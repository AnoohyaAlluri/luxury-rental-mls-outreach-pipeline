# 🏗️ Data Architecture

## Overview

This project uses a medallion-style data architecture to organize the workflow from raw listing data to campaign-ready outreach outputs.

The goal is to show how a luxury rental lead workflow can be structured as a repeatable data system, not just a manual spreadsheet process.

```text
Bronze Layer
Raw MLS-style listing exports

        ↓

Silver Layer
Cleaned and standardized lead records

        ↓

Gold Layer
Campaign-ready outreach queue

        ↓

Analytics Layer
Campaign readiness and performance summary
```

---

## 🥉 Bronze Layer: Raw Listing Data

The Bronze Layer stores synthetic raw MLS-style listing exports.

These files represent the type of unprocessed listing data that might be exported before cleanup, validation, segmentation, or campaign preparation.

### Folder

```text
datasets/raw/
```

### Example File

```text
raw_mls_luxury_listings_mock.csv
```

### Example Fields

| Field          | Description                                     |
| -------------- | ----------------------------------------------- |
| listing_id     | Synthetic listing identifier                    |
| listing_status | Listing status, such as New Listing or Leased   |
| listing_date   | Date associated with the listing                |
| city           | Listing city                                    |
| property_type  | Property type, such as SFR, condo, or townhouse |
| listing_price  | Monthly listed rent or lease amount             |
| agent_name     | Synthetic agent full name                       |
| agent_email    | Synthetic agent email                           |
| agent_phone    | Synthetic agent phone number                    |
| brokerage      | Synthetic brokerage name                        |
| source_file    | Mock source file name                           |

### Purpose

The Bronze Layer keeps raw data separate from cleaned data so the pipeline can preserve the original input structure and support transparent transformation steps.

---

## 🥈 Silver Layer: Cleaned and Standardized Records

The Silver Layer stores cleaned lead records after field standardization, validation, and enrichment.

### Folder

```text
datasets/cleaned/
```

### Example File

```text
cleaned_luxury_listing_leads.csv
```

### Cleaning Logic

The Silver Layer applies the following transformations:

| Transformation            | Purpose                                                              |
| ------------------------- | -------------------------------------------------------------------- |
| Standardize column names  | Converts fields into consistent snake_case naming                    |
| Trim text fields          | Removes extra spaces from names, cities, emails, and brokerage names |
| Normalize city names      | Creates consistent city values for segmentation                      |
| Normalize phone numbers   | Converts phone numbers into 10-digit cleaned format when possible    |
| Validate emails           | Flags invalid or missing email addresses                             |
| Split agent names         | Creates agent first and last name fields for personalization         |
| Create listing age fields | Calculates how old the listing is                                    |
| Create price bands        | Groups listings into pricing tiers                                   |
| Flag duplicates           | Identifies duplicate listing or contact records                      |
| Assign QA status          | Marks records as PASS, REVIEW, or FAIL                               |

### Purpose

The Silver Layer creates a reliable, standardized lead table that can be used for campaign logic and reporting.

---

## 🥇 Gold Layer: Campaign-Ready Outreach Queue

The Gold Layer creates the final outreach-ready campaign queue.

### Folder

```text
outputs/
```

### Example File

```text
campaign_queue_mock.csv
```

### Example Fields

| Field             | Description                                     |
| ----------------- | ----------------------------------------------- |
| lead_id           | Synthetic lead identifier                       |
| campaign_type     | New Listing or Leased Follow-up                 |
| listing_status    | Standardized listing status                     |
| agent_first_name  | Cleaned first name for outreach personalization |
| agent_last_name   | Cleaned last name                               |
| agent_email_clean | Validated synthetic email                       |
| agent_phone_clean | Normalized synthetic phone number               |
| brokerage_clean   | Cleaned brokerage name                          |
| city_cluster      | Grouped city or market area                     |
| price_band        | Listing price category                          |
| listing_age_days  | Age of listing in days                          |
| outreach_priority | High, Medium, or Low                            |
| email_available   | TRUE or FALSE                                   |
| phone_available   | TRUE or FALSE                                   |
| qa_status         | PASS, REVIEW, or FAIL                           |
| send_status       | Not Sent, Sent, Opened, Clicked, or Replied     |
| follow_up_status  | Not Needed, Needed, Sent, or Completed          |

### Purpose

The Gold Layer turns cleaned listing data into a structured queue that can support outreach, follow-up, and campaign reporting.

---

## 📊 Analytics Layer: Campaign Summary

The Analytics Layer summarizes campaign readiness and performance.

### Folder

```text
datasets/analytics/
```

### Example File

```text
campaign_summary_mock.csv
```

### Example Metrics

| Metric                   | Description                          |
| ------------------------ | ------------------------------------ |
| total_leads              | Total records in the campaign queue  |
| valid_email_count        | Leads with usable email addresses    |
| missing_email_count      | Leads missing usable email addresses |
| valid_phone_count        | Leads with usable phone numbers      |
| duplicate_count          | Records flagged as duplicates        |
| qa_pass_count            | Records that passed QA               |
| qa_fail_count            | Records that failed QA               |
| qa_pass_rate             | Percentage of records that passed QA |
| high_priority_count      | Leads marked as high priority        |
| sent_count               | Emails marked as sent                |
| opened_count             | Emails marked as opened              |
| clicked_count            | Leads with click activity            |
| replied_count            | Leads with reply activity            |
| follow_up_required_count | Leads requiring follow-up            |

### Purpose

The Analytics Layer gives a high-level view of whether the campaign queue is ready, where data quality gaps exist, and how outreach is performing.

---

## 🔄 End-to-End Flow

```text
datasets/raw/raw_mls_luxury_listings_mock.csv
        ↓
scripts/bronze/01_load_raw_mls_exports.py
        ↓
scripts/silver/02_clean_and_standardize_leads.py
        ↓
datasets/cleaned/cleaned_luxury_listing_leads.csv
        ↓
scripts/gold/03_build_campaign_queue.py
        ↓
outputs/campaign_queue_mock.csv
        ↓
scripts/analytics/04_generate_campaign_summary.py
        ↓
datasets/analytics/campaign_summary_mock.csv
```

---

## 🧪 Quality Control Points

Quality control is applied at multiple points in the pipeline.

### Bronze QA

* Required raw fields are present.
* Listing IDs are not blank.
* Listing statuses are populated.
* Source file values are available.

### Silver QA

* Emails are valid or flagged.
* Phone numbers are normalized or flagged.
* Cities are standardized.
* Duplicate records are identified.
* Price bands are assigned.
* QA status is populated.

### Gold QA

* Campaign type is assigned.
* Outreach priority is assigned.
* Required outreach fields are present.
* Failed records are excluded or marked for review.
* Send and follow-up fields are initialized.

### Analytics QA

* Summary counts match output files.
* QA pass rate is calculated correctly.
* Missing contact counts are visible.
* Follow-up counts are traceable.

---

## 🔒 Public-Safe Design

This architecture is designed for portfolio demonstration only.

All records are synthetic. The structure represents workflow logic without exposing real company data, real MLS exports, real agent contact information, property addresses, Gmail messages, Google Sheets, Apps Script deployment URLs, or internal business records.
