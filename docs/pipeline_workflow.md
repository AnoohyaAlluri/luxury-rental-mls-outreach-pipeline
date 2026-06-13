# 🔄 Pipeline Workflow

## Overview

This document explains the end-to-end workflow for the **Luxury Rental Lead Pipeline & MLS Outreach Automation System**.

The project turns synthetic raw MLS-style luxury rental listing files into cleaned lead records, validated outreach queues, and campaign-ready reporting outputs.

The workflow is designed to show how a marketing operations process can be structured like a repeatable data pipeline.

---

## 🧭 End-to-End Workflow

```text
Raw MLS-style listing files
        ↓
Bronze Layer: Raw data intake
        ↓
Silver Layer: Cleaning and standardization
        ↓
Gold Layer: Campaign-ready outreach queue
        ↓
Automation Logic: Send, open, click, reply, and follow-up tracking
        ↓
Analytics Layer: Campaign readiness and performance reporting
```

---

## 🥉 Step 1: Bronze Layer

### Goal

Load synthetic raw MLS-style luxury rental listing data into the project without changing the original input structure.

### Input

```text
datasets/raw/raw_mls_luxury_listings_mock.csv
```

### Key Actions

* Read raw listing data
* Preserve original source fields
* Confirm required columns exist
* Flag blank listing IDs
* Keep raw values unchanged for traceability

### Example Raw Fields

* listing_id
* listing_status
* listing_date
* city
* property_type
* listing_price
* agent_name
* agent_email
* agent_phone
* brokerage
* source_file

### Output

The raw dataset is passed into the Silver Layer for cleaning and standardization.

---

## 🥈 Step 2: Silver Layer

### Goal

Clean, standardize, and validate the raw listing data so it can be used for campaign preparation.

### Input

```text
datasets/raw/raw_mls_luxury_listings_mock.csv
```

### Key Actions

* Convert column names to snake_case
* Trim extra spaces from text fields
* Standardize city names
* Standardize property type values
* Normalize phone numbers
* Validate email format
* Split agent full name into first and last name
* Create price bands
* Create listing age fields
* Flag missing email and phone values
* Flag duplicate records
* Assign QA status

### Example Cleaning Rules

| Rule                | Logic                                                                 |
| ------------------- | --------------------------------------------------------------------- |
| Email validation    | Email must include `@` and a valid domain pattern                     |
| Phone normalization | Phone must resolve to 10 digits when possible                         |
| City cleanup        | City names are converted into consistent title case                   |
| Price banding       | Listing prices are grouped into ranges such as `$8K-$15K` and `$15K+` |
| QA status           | Records are marked as `PASS`, `REVIEW`, or `FAIL`                     |

### Output

```text
datasets/cleaned/cleaned_luxury_listing_leads.csv
```

---

## 🥇 Step 3: Gold Layer

### Goal

Convert cleaned lead records into a campaign-ready outreach queue.

### Input

```text
datasets/cleaned/cleaned_luxury_listing_leads.csv
```

### Key Actions

* Create synthetic lead IDs
* Assign campaign type
* Assign city cluster
* Assign outreach priority
* Keep only campaign-ready fields
* Initialize outreach tracking fields
* Separate records that need review
* Prepare records for outreach and reporting

### Campaign Types

| Campaign Type    | Description                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| New Listing      | Outreach connected to current luxury rental opportunities              |
| Leased Follow-up | Follow-up workflow connected to recently leased luxury rental listings |

### Priority Logic

| Priority | Example Logic                                              |
| -------- | ---------------------------------------------------------- |
| High     | Valid email, high price band, target city cluster, QA pass |
| Medium   | Valid email but lower priority market or missing phone     |
| Review   | Missing contact details or duplicate signal                |
| Low      | Outside target criteria or insufficient data               |

### Output

```text
outputs/campaign_queue_mock.csv
```

---

## ⚙️ Step 4: Outreach Automation Logic

### Goal

Represent the outreach tracking workflow without exposing real Apps Script code, Gmail data, tracking pixels, or deployment URLs.

### Input

```text
outputs/campaign_queue_mock.csv
```

### Tracking Fields

* send_status
* send_date
* message_id
* open_count
* first_open_date
* last_open_date
* click_count
* first_click_date
* last_click_date
* reply_status
* reply_date
* follow_up_status
* final_outcome

### Status Flow

```text
Not Sent
   ↓
Sent
   ↓
Opened
   ↓
Clicked
   ↓
Replied
```

A lead may also move into:

```text
Follow-up Required
   ↓
Follow-up Sent
   ↓
Completed
```

### Automation Concepts

* Batched sending logic
* Message ID generation
* Open tracking concept
* Click tracking concept
* Reply tracking concept
* Follow-up status updates
* Final outcome classification

### Public-Safe Note

The public version will use pseudocode only. It will not include real Gmail threads, Apps Script deployment links, tracking URLs, execution logs, or internal scripts.

---

## 📊 Step 5: Analytics Layer

### Goal

Summarize campaign readiness, data quality, and outreach performance.

### Input

```text
outputs/campaign_queue_mock.csv
```

### Key Actions

* Count total campaign leads
* Count valid emails
* Count missing emails
* Count valid phones
* Count missing phones
* Count duplicate records
* Count QA pass, review, and fail records
* Calculate QA pass rate
* Count high-priority leads
* Count sent, opened, clicked, and replied records
* Count leads requiring follow-up

### Output

```text
datasets/analytics/campaign_summary_mock.csv
```

---

## 📈 Example Campaign Metrics

| Metric                   | Purpose                                |
| ------------------------ | -------------------------------------- |
| total_leads              | Shows size of the campaign queue       |
| valid_email_count        | Shows how many leads are email-ready   |
| missing_email_count      | Shows contact-data gaps                |
| qa_pass_rate             | Shows pipeline data quality            |
| high_priority_count      | Shows strongest outreach opportunities |
| sent_count               | Shows campaign execution volume        |
| opened_count             | Shows early engagement                 |
| clicked_count            | Shows intent signal                    |
| replied_count            | Shows direct response                  |
| follow_up_required_count | Shows next-step workload               |

---

## 🧪 QA Checkpoints

### Bronze QA

* Required raw fields exist
* Listing ID is not blank
* Listing status is not blank
* Source file is populated

### Silver QA

* Email format is valid or flagged
* Phone format is valid or flagged
* City value is standardized
* Property type is standardized
* Price band is assigned
* Duplicate status is checked
* QA status is populated

### Gold QA

* Lead ID is assigned
* Campaign type is assigned
* Outreach priority is assigned
* Send status is initialized
* Follow-up status is initialized
* Failed records are excluded or marked for review

### Analytics QA

* Summary counts match campaign queue records
* QA pass rate is calculated correctly
* Follow-up count is traceable
* Engagement metrics are grouped consistently

---

## 🧱 Workflow Summary

```text
1. Load raw synthetic MLS-style listing exports
2. Clean and standardize listing, agent, and contact fields
3. Validate records using QA rules
4. Segment leads into campaign types
5. Build campaign-ready outreach queue
6. Initialize tracking fields
7. Apply outreach automation logic
8. Generate campaign readiness and performance summary
```

---

## 🔒 Confidentiality Design

This workflow is a public-safe reconstruction of a real growth operations process.

The repository does not include real company data, MLS exports, agent names, emails, phone numbers, property addresses, Gmail content, Google Sheets, Apps Script deployment URLs, tracking URLs, execution logs, or internal business records.

All examples are synthetic and designed only to demonstrate the workflow logic.
