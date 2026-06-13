import pandas as pd
from pathlib import Path


CAMPAIGN_QUEUE_FILE = Path("outputs/campaign_queue_mock.csv")
SUMMARY_FILE = Path("datasets/analytics/campaign_summary_mock.csv")


def safe_rate(numerator, denominator):
    """Calculate a percentage safely without division errors."""
    if denominator == 0:
        return 0.0

    return round((numerator / denominator) * 100, 2)


def count_if(df, column, value):
    """Count rows where a column equals a specific value."""
    if column not in df.columns:
        return 0

    return int((df[column] == value).sum())


def count_true(df, column):
    """Count TRUE values in a boolean column."""
    if column not in df.columns:
        return 0

    return int(df[column].sum())


def build_summary(df):
    """Create one campaign summary row from the campaign queue."""

    total_leads = len(df)

    valid_email_count = count_true(df, "email_available")
    missing_email_count = total_leads - valid_email_count

    valid_phone_count = count_true(df, "phone_available")
    missing_phone_count = total_leads - valid_phone_count

    duplicate_count = count_true(df, "duplicate_flag")

    qa_pass_count = count_if(df, "qa_status", "PASS")
    qa_review_count = count_if(df, "qa_status", "REVIEW")
    qa_fail_count = count_if(df, "qa_status", "FAIL")

    high_priority_count = count_if(df, "outreach_priority", "High")
    medium_priority_count = count_if(df, "outreach_priority", "Medium")
    review_priority_count = count_if(df, "outreach_priority", "Review")
    low_priority_count = count_if(df, "outreach_priority", "Low")

    sent_count = count_if(df, "send_status", "Sent")
    opened_count = count_if(df, "send_status", "Opened")
    clicked_count = count_if(df, "send_status", "Clicked")
    replied_count = count_if(df, "send_status", "Replied")
    excluded_count = count_if(df, "send_status", "Excluded")
    not_sent_count = count_if(df, "send_status", "Not Sent")

    follow_up_required_count = count_if(df, "follow_up_status", "Follow-up Required")
    follow_up_sent_count = count_if(df, "follow_up_status", "Follow-up Sent")

    outreach_ready_count = int(
        (
            (df["qa_status"] == "PASS")
            & (df["email_available"] == True)
            & (df["send_status"] == "Not Sent")
        ).sum()
    )

    summary = {
        "campaign_name": "Luxury Rental MLS Outreach Pipeline",
        "total_leads": total_leads,
        "valid_email_count": valid_email_count,
        "missing_email_count": missing_email_count,
        "valid_phone_count": valid_phone_count,
        "missing_phone_count": missing_phone_count,
        "duplicate_count": duplicate_count,
        "qa_pass_count": qa_pass_count,
        "qa_review_count": qa_review_count,
        "qa_fail_count": qa_fail_count,
        "qa_pass_rate": safe_rate(qa_pass_count, total_leads),
        "high_priority_count": high_priority_count,
        "medium_priority_count": medium_priority_count,
        "review_priority_count": review_priority_count,
        "low_priority_count": low_priority_count,
        "outreach_ready_count": outreach_ready_count,
        "not_sent_count": not_sent_count,
        "sent_count": sent_count,
        "opened_count": opened_count,
        "clicked_count": clicked_count,
        "replied_count": replied_count,
        "excluded_count": excluded_count,
        "follow_up_required_count": follow_up_required_count,
        "follow_up_sent_count": follow_up_sent_count,
        "email_readiness_rate": safe_rate(valid_email_count, total_leads),
        "phone_readiness_rate": safe_rate(valid_phone_count, total_leads),
        "duplicate_rate": safe_rate(duplicate_count, total_leads),
        "outreach_ready_rate": safe_rate(outreach_ready_count, total_leads),
        "open_rate": safe_rate(opened_count, sent_count),
        "click_rate": safe_rate(clicked_count, sent_count),
        "reply_rate": safe_rate(replied_count, sent_count),
    }

    return pd.DataFrame([summary])


def main():
    if not CAMPAIGN_QUEUE_FILE.exists():
        raise FileNotFoundError(
            f"Campaign queue file not found: {CAMPAIGN_QUEUE_FILE}. "
            "Run scripts/gold/03_build_campaign_queue.py first."
        )

    df = pd.read_csv(CAMPAIGN_QUEUE_FILE)

    summary_df = build_summary(df)

    SUMMARY_FILE.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(SUMMARY_FILE, index=False)

    print(f"Campaign summary created: {SUMMARY_FILE}")
    print(summary_df.to_string(index=False))


if __name__ == "__main__":
    main()
