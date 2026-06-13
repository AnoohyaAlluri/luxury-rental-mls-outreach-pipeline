import pandas as pd
from pathlib import Path


CLEANED_FILE = Path("datasets/cleaned/cleaned_luxury_listing_leads.csv")
CAMPAIGN_QUEUE_FILE = Path("outputs/campaign_queue_mock.csv")


def create_lead_id(index):
    """Create a synthetic lead ID for the public-safe campaign queue."""
    return f"LUX-{index + 1:04d}"


def assign_campaign_type(listing_status):
    """Assign campaign type based on cleaned listing status."""
    status = str(listing_status).strip().lower()

    if "leased" in status:
        return "Leased Follow-up"

    if "new" in status:
        return "New Listing"

    return "Review Needed"


def assign_outreach_priority(row):
    """
    Assign outreach priority using public-safe business logic.

    High priority:
    - QA passed
    - Email available
    - $15K+ price band
    - Target luxury city cluster

    Medium priority:
    - QA passed
    - Email available
    - $8K-$15K or valid market signal

    Review:
    - Record needs QA review

    Low:
    - Weak contact readiness or outside preferred criteria
    """
    if row["qa_status"] == "FAIL":
        return "Low"

    if row["qa_status"] == "REVIEW":
        return "Review"

    if (
        row["qa_status"] == "PASS"
        and row["email_available"]
        and row["price_band"] == "$15K+"
        and row["city_cluster"] in ["Westside Luxury", "Beach Luxury"]
    ):
        return "High"

    if row["qa_status"] == "PASS" and row["email_available"]:
        return "Medium"

    return "Low"


def initialize_send_status(row):
    """Initialize outreach send status."""
    if row["qa_status"] == "PASS" and row["email_available"]:
        return "Not Sent"

    return "Excluded"


def initialize_follow_up_status(row):
    """Initialize follow-up status."""
    if row["qa_status"] == "PASS" and row["email_available"]:
        return "Not Started"

    return "Not Needed"


def main():
    if not CLEANED_FILE.exists():
        raise FileNotFoundError(
            f"Cleaned file not found: {CLEANED_FILE}. "
            "Run scripts/silver/02_clean_and_standardize_leads.py first."
        )

    df = pd.read_csv(CLEANED_FILE)

    df["lead_id"] = [create_lead_id(i) for i in range(len(df))]
    df["campaign_type"] = df["listing_status_clean"].apply(assign_campaign_type)
    df["outreach_priority"] = df.apply(assign_outreach_priority, axis=1)
    df["send_status"] = df.apply(initialize_send_status, axis=1)
    df["follow_up_status"] = df.apply(initialize_follow_up_status, axis=1)

    campaign_columns = [
        "lead_id",
        "listing_id",
        "campaign_type",
        "listing_status_clean",
        "agent_first_name",
        "agent_last_name",
        "agent_email_clean",
        "agent_phone_clean",
        "brokerage_clean",
        "city_clean",
        "city_cluster",
        "property_type_clean",
        "listing_price",
        "price_band",
        "listing_age_days",
        "outreach_priority",
        "email_available",
        "phone_available",
        "duplicate_flag",
        "qa_status",
        "qa_notes",
        "send_status",
        "follow_up_status",
    ]

    campaign_queue = df[campaign_columns]

    CAMPAIGN_QUEUE_FILE.parent.mkdir(parents=True, exist_ok=True)
    campaign_queue.to_csv(CAMPAIGN_QUEUE_FILE, index=False)

    print(f"Campaign queue created: {CAMPAIGN_QUEUE_FILE}")
    print(f"Rows in campaign queue: {len(campaign_queue)}")
    print("\nOutreach priority counts:")
    print(campaign_queue["outreach_priority"].value_counts())
    print("\nSend status counts:")
    print(campaign_queue["send_status"].value_counts())


if __name__ == "__main__":
    main()
