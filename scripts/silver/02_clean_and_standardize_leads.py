import pandas as pd
import re
from datetime import datetime
from pathlib import Path


RAW_FILE = Path("datasets/raw/raw_mls_luxury_listings_mock.csv")
CLEANED_FILE = Path("datasets/cleaned/cleaned_luxury_listing_leads.csv")


REFERENCE_DATE = datetime(2026, 4, 30)


CITY_CLUSTER_MAP = {
    "Beverly Hills": "Westside Luxury",
    "Beverly Hills Po": "Westside Luxury",
    "Santa Monica": "Westside Luxury",
    "Brentwood": "Westside Luxury",
    "Pacific Palisades": "Westside Luxury",
    "Malibu": "Beach Luxury",
    "West Hollywood": "Central Westside",
    "West La": "Westside",
    "Bel Air": "Westside Luxury",
    "Venice": "Beach Luxury",
}


PROPERTY_TYPE_MAP = {
    "single family": "SFR",
    "single family residence": "SFR",
    "sfr": "SFR",
    "condo": "Condo",
    "townhouse": "Townhouse",
}


def clean_text(value):
    """Trim text and convert blank values to empty strings."""
    if pd.isna(value):
        return ""
    return str(value).strip()


def normalize_city(value):
    """Normalize raw city names into title case."""
    value = clean_text(value)
    if not value:
        return ""

    return value.lower().title()


def normalize_property_type(value):
    """Map raw property type values into standard categories."""
    value = clean_text(value).lower()

    if value in PROPERTY_TYPE_MAP:
        return PROPERTY_TYPE_MAP[value]

    return "Review Needed" if value else "Unknown"


def normalize_phone(value):
    """Keep only digits and return 10-digit phone numbers when possible."""
    value = clean_text(value)
    digits = re.sub(r"\D", "", value)

    if len(digits) == 10:
        return digits

    return ""


def is_valid_email(value):
    """Basic email validation for synthetic portfolio data."""
    value = clean_text(value).lower()

    if not value:
        return False

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, value) is not None


def clean_email(value):
    """Return lowercase email only when format is valid."""
    value = clean_text(value).lower()

    if is_valid_email(value):
        return value

    return ""


def split_first_name(value):
    """Extract first name from a synthetic full name field."""
    value = clean_text(value)

    if not value:
        return ""

    return value.split()[0]


def split_last_name(value):
    """Extract last name from a synthetic full name field."""
    value = clean_text(value)

    if not value:
        return ""

    parts = value.split()
    return parts[-1] if len(parts) > 1 else ""


def create_price_band(value):
    """Create simple luxury rental price bands."""
    if pd.isna(value):
        return "Unknown"

    try:
        price = float(value)
    except ValueError:
        return "Unknown"

    if price >= 15000:
        return "$15K+"
    if price >= 8000:
        return "$8K-$15K"
    if price > 0:
        return "Under $8K"

    return "Unknown"


def calculate_listing_age_days(value):
    """Calculate age of listing using a fixed reference date for reproducibility."""
    try:
        listing_date = pd.to_datetime(value)
    except Exception:
        return None

    return (REFERENCE_DATE - listing_date).days


def assign_qa_status(row):
    """Assign PASS, REVIEW, or FAIL based on key data quality rules."""
    if not row["listing_id"]:
        return "FAIL"

    if not row["listing_status_clean"]:
        return "FAIL"

    if not row["agent_first_name"]:
        return "FAIL"

    if not row["email_available"] and not row["phone_available"]:
        return "FAIL"

    if row["duplicate_flag"]:
        return "REVIEW"

    if not row["email_available"]:
        return "REVIEW"

    if row["price_band"] == "Unknown":
        return "REVIEW"

    if not row["city_clean"]:
        return "REVIEW"

    return "PASS"


def create_qa_notes(row):
    """Create public-safe QA notes."""
    notes = []

    if not row["listing_id"]:
        notes.append("Missing listing ID")

    if not row["listing_status_clean"]:
        notes.append("Missing listing status")

    if not row["agent_first_name"]:
        notes.append("Missing agent name")

    if not row["email_available"]:
        notes.append("Missing or invalid email")

    if not row["phone_available"]:
        notes.append("Missing or invalid phone")

    if row["duplicate_flag"]:
        notes.append("Duplicate listing ID")

    if row["price_band"] == "Unknown":
        notes.append("Missing or invalid listing price")

    if not row["city_clean"]:
        notes.append("Missing city")

    if not notes:
        return "Valid email and phone"

    return "; ".join(notes)


def main():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw file not found: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE)

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    df["listing_id"] = df["listing_id"].apply(clean_text)
    df["listing_status_clean"] = df["listing_status"].apply(clean_text)
    df["listing_date"] = pd.to_datetime(df["listing_date"], errors="coerce")
    df["city_clean"] = df["city"].apply(normalize_city)
    df["city_cluster"] = df["city_clean"].map(CITY_CLUSTER_MAP).fillna("Review Needed")
    df["property_type_clean"] = df["property_type"].apply(normalize_property_type)
    df["listing_price"] = pd.to_numeric(df["listing_price"], errors="coerce")
    df["price_band"] = df["listing_price"].apply(create_price_band)

    df["agent_name"] = df["agent_name"].apply(clean_text)
    df["agent_first_name"] = df["agent_name"].apply(split_first_name)
    df["agent_last_name"] = df["agent_name"].apply(split_last_name)

    df["agent_email_clean"] = df["agent_email"].apply(clean_email)
    df["agent_phone_clean"] = df["agent_phone"].apply(normalize_phone)
    df["brokerage_clean"] = df["brokerage"].apply(clean_text)

    df["email_available"] = df["agent_email_clean"] != ""
    df["phone_available"] = df["agent_phone_clean"] != ""

    df["duplicate_flag"] = df.duplicated(subset=["listing_id"], keep=False)
    df["listing_age_days"] = df["listing_date"].apply(calculate_listing_age_days)

    df["qa_status"] = df.apply(assign_qa_status, axis=1)
    df["qa_notes"] = df.apply(create_qa_notes, axis=1)

    cleaned_columns = [
        "listing_id",
        "listing_status_clean",
        "listing_date",
        "city_clean",
        "city_cluster",
        "property_type_clean",
        "listing_price",
        "price_band",
        "agent_first_name",
        "agent_last_name",
        "agent_email_clean",
        "agent_phone_clean",
        "brokerage_clean",
        "email_available",
        "phone_available",
        "duplicate_flag",
        "listing_age_days",
        "qa_status",
        "qa_notes",
    ]

    cleaned_df = df[cleaned_columns]

    CLEANED_FILE.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(CLEANED_FILE, index=False)

    print(f"Cleaned dataset created: {CLEANED_FILE}")
    print(f"Rows processed: {len(cleaned_df)}")
    print("QA status counts:")
    print(cleaned_df["qa_status"].value_counts())


if __name__ == "__main__":
    main()
