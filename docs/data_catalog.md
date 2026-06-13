# 📚 Data Catalog

## Overview

This data catalog defines the synthetic datasets used in the **Luxury Rental Lead Pipeline & MLS Outreach Automation System**.

The purpose of this file is to document each dataset, field, data type, and business meaning so the project is easy to understand for recruiters, analysts, engineers, and portfolio reviewers.

All data in this repository is synthetic and public-safe.

---

## 📁 Dataset Inventory

| Dataset                            | Folder                | Description                                          |
| ---------------------------------- | --------------------- | ---------------------------------------------------- |
| `raw_mls_luxury_listings_mock.csv` | `datasets/raw/`       | Synthetic raw MLS-style luxury rental listing export |
| `cleaned_luxury_listing_leads.csv` | `datasets/cleaned/`   | Cleaned and standardized lead records                |
| `campaign_queue_mock.csv`          | `outputs/`            | Campaign-ready outreach queue                        |
| `campaign_summary_mock.csv`        | `datasets/analytics/` | Campaign readiness and performance summary           |

---

# 🥉 Dataset 1: `raw_mls_luxury_listings_mock.csv`

## Purpose

This dataset represents the raw MLS-style listing export before cleaning, validation, or campaign preparation.

The file intentionally includes realistic data quality issues such as inconsistent casing, missing emails, mixed phone formats, and uneven listing-status values.

## Location

```text
datasets/raw/raw_mls_luxury_listings_mock.csv
```

## Fields

| Field            | Type    | Description                    | Example                    |
| ---------------- | ------- | ------------------------------ | -------------------------- |
| `listing_id`     | string  | Synthetic listing identifier   | `MLS1001`                  |
| `listing_status` | string  | Raw listing status             | `New Listing`              |
| `listing_date`   | date    | Listing or lease date          | `2026-04-15`               |
| `city`           | string  | Raw city value                 | `beverly hills`            |
| `property_type`  | string  | Raw property type              | `Single Family`            |
| `listing_price`  | integer | Synthetic monthly rental price | `18000`                    |
| `agent_name`     | string  | Synthetic agent full name      | `Jordan Lee`               |
| `agent_email`    | string  | Synthetic agent email          | `jordan.lee@example.com`   |
| `agent_phone`    | string  | Synthetic phone number         | `(310) 555-0198`           |
| `brokerage`      | string  | Synthetic brokerage name       | `Example Realty Group`     |
| `source_file`    | string  | Mock file source name          | `week_01_new_listings.csv` |

---

# 🥈 Dataset 2: `cleaned_luxury_listing_leads.csv`

## Purpose

This dataset stores cleaned and standardized lead records after transformation.

It is used as the reliable intermediate table before campaign queue creation.

## Location

```text
datasets/cleaned/cleaned_luxury_listing_leads.csv
```

## Fields

| Field                  | Type    | Description                       | Example                  |
| ---------------------- | ------- | --------------------------------- | ------------------------ |
| `listing_id`           | string  | Synthetic listing identifier      | `MLS1001`                |
| `listing_status_clean` | string  | Standardized listing status       | `new_listing`            |
| `listing_date`         | date    | Standardized listing date         | `2026-04-15`             |
| `city_clean`           | string  | Standardized city name            | `Beverly Hills`          |
| `city_cluster`         | string  | Market cluster for segmentation   | `Westside Luxury`        |
| `property_type_clean`  | string  | Standardized property type        | `SFR`                    |
| `listing_price`        | integer | Synthetic monthly rental price    | `18000`                  |
| `price_band`           | string  | Listing price category            | `$15K+`                  |
| `agent_first_name`     | string  | Cleaned first name                | `Jordan`                 |
| `agent_last_name`      | string  | Cleaned last name                 | `Lee`                    |
| `agent_email_clean`    | string  | Standardized email                | `jordan.lee@example.com` |
| `agent_phone_clean`    | string  | 10-digit normalized phone         | `3105550198`             |
| `brokerage_clean`      | string  | Cleaned brokerage name            | `Example Realty Group`   |
| `email_available`      | boolean | Whether a usable email exists     | `TRUE`                   |
| `phone_available`      | boolean | Whether a usable phone exists     | `TRUE`                   |
| `duplicate_flag`       | boolean | Whether record appears duplicated | `FALSE`                  |
| `listing_age_days`     | integer | Days since listing date           | `6`                      |
| `qa_status`            | string  | PASS, REVIEW, or FAIL             | `PASS`                   |
| `qa_notes`             | string  | Public-safe QA explanation        | `Valid email and phone`  |

---

# 🥇 Dataset 3: `campaign_queue_mock.csv`

## Purpose

This dataset is the campaign-ready outreach queue.

It contains the cleaned fields needed to support outreach, follow-up, tracking, and reporting.

## Location

```text
outputs/campaign_queue_mock.csv
```

## Fields

| Field               | Type    | Description                    | Example                  |
| ------------------- | ------- | ------------------------------ | ------------------------ |
| `lead_id`           | string  | Synthetic campaign lead ID     | `LUX-0001`               |
| `listing_id`        | string  | Synthetic listing ID           | `MLS1001`                |
| `campaign_type`     | string  | Outreach segment               | `New Listing`            |
| `agent_first_name`  | string  | First name for personalization | `Jordan`                 |
| `agent_last_name`   | string  | Last name for tracking         | `Lee`                    |
| `agent_email_clean` | string  | Outreach email                 | `jordan.lee@example.com` |
| `agent_phone_clean` | string  | Normalized phone               | `3105550198`             |
| `brokerage_clean`   | string  | Cleaned brokerage              | `Example Realty Group`   |
| `city_cluster`      | string  | Market segment                 | `Westside Luxury`        |
| `price_band`        | string  | Price category                 | `$15K+`                  |
| `listing_age_days`  | integer | Days since listing date        | `6`                      |
| `outreach_priority` | string  | High, Medium, or Low           | `High`                   |
| `email_available`   | boolean | Email readiness flag           | `TRUE`                   |
| `phone_available`   | boolean | Phone readiness flag           | `TRUE`                   |
| `qa_status`         | string  | Record quality result          | `PASS`                   |
| `send_status`       | string  | Outreach state                 | `Not Sent`               |
| `follow_up_status`  | string  | Follow-up state                | `Not Started`            |

---

# 📊 Dataset 4: `campaign_summary_mock.csv`

## Purpose

This dataset summarizes campaign readiness and outreach performance.

It is used to show how the pipeline can produce analytics-ready reporting.

## Location

```text
datasets/analytics/campaign_summary_mock.csv
```

## Fields

| Field                      | Type    | Description                          | Example               |
| -------------------------- | ------- | ------------------------------------ | --------------------- |
| `campaign_name`            | string  | Name of campaign segment             | `Luxury New Listings` |
| `total_leads`              | integer | Total leads in queue                 | `25`                  |
| `valid_email_count`        | integer | Leads with usable email              | `22`                  |
| `missing_email_count`      | integer | Leads without usable email           | `3`                   |
| `valid_phone_count`        | integer | Leads with usable phone              | `21`                  |
| `missing_phone_count`      | integer | Leads without usable phone           | `4`                   |
| `duplicate_count`          | integer | Duplicate records flagged            | `2`                   |
| `qa_pass_count`            | integer | Records that passed QA               | `20`                  |
| `qa_fail_count`            | integer | Records that failed QA               | `2`                   |
| `qa_review_count`          | integer | Records requiring review             | `3`                   |
| `qa_pass_rate`             | decimal | Percentage of records that passed QA | `80.0`                |
| `high_priority_count`      | integer | High-priority leads                  | `12`                  |
| `sent_count`               | integer | Emails sent                          | `15`                  |
| `opened_count`             | integer | Emails opened                        | `9`                   |
| `clicked_count`            | integer | Emails clicked                       | `3`                   |
| `replied_count`            | integer | Replies received                     | `2`                   |
| `follow_up_required_count` | integer | Leads requiring follow-up            | `6`                   |

---

## 🧪 Data Quality Fields

The following fields support QA and validation across the project:

| Field               | Purpose                                                 |
| ------------------- | ------------------------------------------------------- |
| `email_available`   | Flags whether the record has a usable email             |
| `phone_available`   | Flags whether the record has a usable phone             |
| `duplicate_flag`    | Flags duplicate or repeated records                     |
| `qa_status`         | Shows whether the record passes, fails, or needs review |
| `qa_notes`          | Explains the QA issue in public-safe language           |
| `outreach_priority` | Prioritizes records for campaign execution              |
| `follow_up_status`  | Tracks next-step readiness                              |

---

## 🔒 Confidentiality Note

This data catalog documents synthetic data only.

It does not describe or expose real MLS exports, real agent records, real property addresses, real phone numbers, real emails, internal Google Sheets, Gmail messages, tracking logs, or confidential Westside Property Management files.
