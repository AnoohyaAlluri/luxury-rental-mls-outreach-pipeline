from pathlib import Path

import pandas as pd


RAW_FILE = Path("datasets/raw/raw_mls_luxury_listings_mock.csv")
CLEANED_FILE = Path("datasets/cleaned/cleaned_luxury_listing_leads.csv")
CAMPAIGN_QUEUE_FILE = Path("outputs/campaign_queue_mock.csv")
SUMMARY_FILE = Path("datasets/analytics/campaign_summary_mock.csv")


def test_raw_file_exists():
    assert RAW_FILE.exists(), f"Missing raw file: {RAW_FILE}"


def test_raw_required_columns_exist():
    df = pd.read_csv(RAW_FILE)

    required_columns = {
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

    missing_columns = required_columns - set(df.columns)

    assert not missing_columns, f"Missing raw columns: {missing_columns}"


def test_cleaned_file_exists_after_pipeline_run():
    assert CLEANED_FILE.exists(), (
        f"Missing cleaned file: {CLEANED_FILE}. "
        "Run scripts/silver/02_clean_and_standardize_leads.py first."
    )


def test_cleaned_required_columns_exist():
    df = pd.read_csv(CLEANED_FILE)

    required_columns = {
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
    }

    missing_columns = required_columns - set(df.columns)

    assert not missing_columns, f"Missing cleaned columns: {missing_columns}"


def test_qa_status_values_are_valid():
    df = pd.read_csv(CLEANED_FILE)

    valid_statuses = {"PASS", "REVIEW", "FAIL"}
    actual_statuses = set(df["qa_status"].dropna().unique())

    invalid_statuses = actual_statuses - valid_statuses

    assert not invalid_statuses, f"Invalid QA statuses found: {invalid_statuses}"


def test_email_available_matches_clean_email_field():
    df = pd.read_csv(CLEANED_FILE)

    df["agent_email_clean"] = df["agent_email_clean"].fillna("")
    expected_email_available = df["agent_email_clean"] != ""

    assert (
        df["email_available"].astype(bool) == expected_email_available
    ).all(), "email_available does not match agent_email_clean"


def test_phone_available_matches_clean_phone_field():
    df = pd.read_csv(CLEANED_FILE)

    df["agent_phone_clean"] = df["agent_phone_clean"].fillna("")
    expected_phone_available = df["agent_phone_clean"] != ""

    assert (
        df["phone_available"].astype(bool) == expected_phone_available
    ).all(), "phone_available does not match agent_phone_clean"


def test_campaign_queue_exists_after_pipeline_run():
    assert CAMPAIGN_QUEUE_FILE.exists(), (
        f"Missing campaign queue file: {CAMPAIGN_QUEUE_FILE}. "
        "Run scripts/gold/03_build_campaign_queue.py first."
    )


def test_campaign_queue_required_columns_exist():
    df = pd.read_csv(CAMPAIGN_QUEUE_FILE)

    required_columns = {
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
    }

    missing_columns = required_columns - set(df.columns)

    assert not missing_columns, f"Missing campaign queue columns: {missing_columns}"


def test_outreach_priority_values_are_valid():
    df = pd.read_csv(CAMPAIGN_QUEUE_FILE)

    valid_priorities = {"High", "Medium", "Review", "Low"}
    actual_priorities = set(df["outreach_priority"].dropna().unique())

    invalid_priorities = actual_priorities - valid_priorities

    assert not invalid_priorities, f"Invalid outreach priorities found: {invalid_priorities}"


def test_send_status_values_are_valid():
    df = pd.read_csv(CAMPAIGN_QUEUE_FILE)

    valid_statuses = {
        "Not Sent",
        "Sent",
        "Opened",
        "Clicked",
        "Replied",
        "Excluded",
    }

    actual_statuses = set(df["send_status"].dropna().unique())
    invalid_statuses = actual_statuses - valid_statuses

    assert not invalid_statuses, f"Invalid send statuses found: {invalid_statuses}"


def test_summary_file_exists_after_pipeline_run():
    assert SUMMARY_FILE.exists(), (
        f"Missing summary file: {SUMMARY_FILE}. "
        "Run scripts/analytics/04_generate_campaign_summary.py first."
    )


def test_summary_total_matches_campaign_queue_count():
    queue_df = pd.read_csv(CAMPAIGN_QUEUE_FILE)
    summary_df = pd.read_csv(SUMMARY_FILE)

    expected_total = len(queue_df)
    actual_total = int(summary_df.loc[0, "total_leads"])

    assert actual_total == expected_total, (
        f"Summary total_leads is {actual_total}, "
        f"but campaign queue has {expected_total} rows."
    )


def test_summary_qa_counts_reconcile():
    summary_df = pd.read_csv(SUMMARY_FILE)

    total_leads = int(summary_df.loc[0, "total_leads"])
    qa_pass_count = int(summary_df.loc[0, "qa_pass_count"])
    qa_review_count = int(summary_df.loc[0, "qa_review_count"])
    qa_fail_count = int(summary_df.loc[0, "qa_fail_count"])

    assert qa_pass_count + qa_review_count + qa_fail_count == total_leads, (
        "QA counts do not reconcile to total leads."
    )
