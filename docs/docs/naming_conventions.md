# 🧾 Naming Conventions

## Overview

This document defines naming standards for the **Luxury Rental Lead Pipeline & MLS Outreach Automation System**.

Consistent naming makes the project easier to read, maintain, test, and explain in a portfolio or technical interview.

This repository uses synthetic data only. File names, field names, IDs, and examples are public-safe.

---

## 📁 Folder Naming

All folder names should use lowercase letters and underscores only when needed.

### Accepted Folder Names

```text
datasets/
datasets/raw/
datasets/cleaned/
datasets/analytics/
docs/
scripts/
scripts/bronze/
scripts/silver/
scripts/gold/
scripts/analytics/
tests/
images/
outputs/
```

### Folder Naming Rules

* Use lowercase letters.
* Use underscores only when a folder name needs multiple words.
* Avoid spaces.
* Avoid special characters.
* Keep names short and descriptive.

---

## 📄 File Naming

File names should be lowercase and descriptive.

### Documentation Files

Documentation files should use snake_case.

```text
requirements.md
data_architecture.md
data_catalog.md
pipeline_workflow.md
qa_rules.md
automation_logic.md
naming_conventions.md
```

### Dataset Files

Dataset files should clearly identify the pipeline layer and purpose.

```text
raw_mls_luxury_listings_mock.csv
cleaned_luxury_listing_leads.csv
campaign_summary_mock.csv
campaign_queue_mock.csv
```

### Script Files

Script files should include a numeric prefix to show execution order.

```text
01_load_raw_mls_exports.py
02_clean_and_standardize_leads.py
03_build_campaign_queue.py
04_generate_campaign_summary.py
```

### Test Files

Test files should start with `test_`.

```text
test_data_quality_rules.py
```

---

## 🧱 Pipeline Layer Naming

This project uses a medallion-style workflow.

| Layer     | Naming Pattern              | Example                            |
| --------- | --------------------------- | ---------------------------------- |
| Bronze    | raw input files             | `raw_mls_luxury_listings_mock.csv` |
| Silver    | cleaned intermediate files  | `cleaned_luxury_listing_leads.csv` |
| Gold      | campaign-ready output files | `campaign_queue_mock.csv`          |
| Analytics | summary reporting files     | `campaign_summary_mock.csv`        |

---

## 🏷️ Column Naming

All dataset column names should use snake_case.

### Good Examples

```text
listing_id
listing_status
listing_date
city_clean
property_type_clean
listing_price
price_band
agent_first_name
agent_last_name
agent_email_clean
agent_phone_clean
brokerage_clean
email_available
phone_available
duplicate_flag
qa_status
qa_notes
outreach_priority
send_status
follow_up_status
final_outcome
```

### Avoid

```text
Listing ID
Agent Email
Phone Number
QA Status
Final Outcome
listingStatus
agent-email
property type
```

---

## 🔢 ID Naming

Synthetic IDs should be easy to read and should not resemble real MLS or internal system IDs.

### Listing IDs

```text
MLS1001
MLS1002
MLS1003
```

### Lead IDs

```text
LUX-0001
LUX-0002
LUX-0003
```

### Message IDs

```text
MSG-0001
MSG-0002
MSG-0003
```

### Batch IDs

```text
BATCH-2026-001
BATCH-2026-002
BATCH-2026-003
```

---

## 🏙️ City and Market Naming

City values should be standardized in title case.

### Raw Values

```text
beverly hills
BEVERLY HILLS
Beverly hills
```

### Clean Value

```text
Beverly Hills
```

### City Cluster Examples

```text
Westside Luxury
Beach Cities
Central LA
Review Needed
```

Use generalized cluster names only. Do not use confidential internal targeting lists.

---

## 💰 Price Band Naming

Price bands should be readable and consistent.

```text
Under $8K
$8K-$15K
$15K+
Unknown
```

Records with missing or invalid listing price should use:

```text
Unknown
```

---

## 🚦 QA Status Naming

QA status values should be uppercase.

```text
PASS
REVIEW
FAIL
```

### Meaning

| QA Status | Meaning                                         |
| --------- | ----------------------------------------------- |
| PASS      | Record is campaign-ready                        |
| REVIEW    | Record needs manual review before outreach      |
| FAIL      | Record should not be used in the campaign queue |

---

## 📬 Outreach Status Naming

Outreach fields should use readable status values.

### Send Status

```text
Not Sent
Sent
Opened
Clicked
Replied
Excluded
```

### Follow-Up Status

```text
Not Started
Not Needed
Follow-up Required
Follow-up Sent
Completed
```

### Final Outcome

```text
Not Sent
Sent
Opened
Clicked
Response Received
Follow-up Required
Follow-up Sent
Excluded
```

---

## 🧪 Boolean Field Naming

Boolean fields should end with a clear indicator such as `_available`, `_flag`, or `_required`.

### Examples

```text
email_available
phone_available
duplicate_flag
follow_up_required
```

Use `TRUE` and `FALSE` in CSV files.

---

## 📊 Metric Naming

Analytics metrics should be lowercase and use snake_case.

```text
total_leads
valid_email_count
missing_email_count
valid_phone_count
missing_phone_count
duplicate_count
qa_pass_count
qa_review_count
qa_fail_count
qa_pass_rate
high_priority_count
sent_count
opened_count
clicked_count
replied_count
follow_up_required_count
```

---

## 🔒 Confidentiality Naming Rules

Do not use real names, real addresses, real emails, real phone numbers, real MLS IDs, real brokerage contact lists, real Gmail subject lines, or internal company IDs.

### Safe Examples

```text
Jordan Lee
jordan.lee@example.com
3105550198
Example Realty Group
MLS1001
LUX-0001
```

### Unsafe Examples

Do not use:

```text
Real agent names
Real agent emails
Real phone numbers
Real property addresses
Real listing IDs
Real company IDs
Real Google Sheet names
Real Gmail subject lines
Real Apps Script deployment IDs
```

---

## ✅ Naming Checklist

Before adding a file or field, confirm:

* The name is public-safe.
* The name is lowercase where possible.
* Dataset columns use snake_case.
* Script files include numeric execution order.
* IDs are synthetic.
* No confidential company information is exposed.
* The name clearly explains the purpose of the file, field, or folder.
