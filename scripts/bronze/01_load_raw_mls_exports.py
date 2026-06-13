from pathlib import Path

import pandas as pd


RAW_FILE = Path("datasets/raw/raw_mls_luxury_listings_mock.csv")
PROFILE_FILE = Path("datasets/analytics/raw_data_profile_mock.csv")


REQUIRED_COLUMNS = {
    "listing_id",
    "listing_status",
    "listing_date",
    "city",
    "property_type",
    "listing_price",
    "agent_name",
    "agent_email",
    "agent_phone",
    "brokerage",
    "source_file",
}


def validate_required_columns(df):
    """Validate that the raw synthetic listing file has the required structure."""
    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required raw columns: {missing_columns}")

    return True


def build_raw_profile(df):
    """Create a public-safe profile of the raw synthetic dataset."""
    total_rows = len(df)

    profile = {
        "dataset_name": "raw_mls_luxury_listings_mock.csv",
        "total_rows": total_rows,
        "total_columns": len(df.columns),
        "blank_listing_id_count": int(df["listing_id"].isna().sum()),
        "blank_listing_status_count": int(df["listing_status"].isna().sum()),
        "blank_city_count": int(df["city"].isna().sum()),
        "blank_agent_name_count": int(df["agent_name"].isna().sum()),
        "blank_agent_email_count": int(df["agent_email"].isna().sum()),
        "blank_agent_phone_count": int(df["agent_phone"].isna().sum()),
        "blank_listing_price_count": int(df["listing_price"].isna().sum()),
        "duplicate_listing_id_count": int(df.duplicated(subset=["listing_id"], keep=False).sum()),
        "unique_source_file_count": int(df["source_file"].nunique()),
    }

    return pd.DataFrame([profile])


def main():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw file not found: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE)

    validate_required_columns(df)

    profile_df = build_raw_profile(df)

    PROFILE_FILE.parent.mkdir(parents=True, exist_ok=True)
    profile_df.to_csv(PROFILE_FILE, index=False)

    print(f"Raw file loaded: {RAW_FILE}")
    print(f"Rows loaded: {len(df)}")
    print(f"Columns loaded: {len(df.columns)}")
    print(f"Raw data profile created: {PROFILE_FILE}")
    print(profile_df.to_string(index=False))


if __name__ == "__main__":
    main()
