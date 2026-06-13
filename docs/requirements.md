# 📋 Project Requirements

## 🏡 Project Name

**Luxury Rental Lead Pipeline & MLS Outreach Automation System**

---

## 🎯 Objective

Build a public-safe data automation and growth operations project that demonstrates how raw MLS-style luxury rental listing exports can be transformed into a structured outreach pipeline.

The project converts synthetic raw listing data into cleaned lead records, campaign-ready outreach queues, QA outputs, and analytics summaries.

---

## 🧩 Business Context

Luxury rental listings can create high-value opportunities for property management outreach, agent referral development, and owner lead generation.

The original business workflow required turning raw listing files into a cleaner system that could support repeatable campaign execution and performance tracking.

This public repository recreates that workflow using only synthetic data.

---

## 🚩 Business Problems

The workflow addresses the following operational issues:

* Raw listing exports are not campaign-ready.
* Listing, agent, and property fields may be inconsistent.
* Contact data may be missing, duplicated, or incorrectly formatted.
* New listings and leased listings require different campaign handling.
* Outreach workflows need clear tracking fields.
* Campaign performance needs summary reporting.
* Sensitive company, MLS, property, and contact data must not be exposed publicly.

---

## ✅ Project Scope

This repository will include:

* Synthetic raw MLS-style listing datasets
* Data cleaning and standardization scripts
* Campaign queue generation logic
* QA validation rules
* Outreach tracking structure
* Campaign analytics summaries
* Public-safe documentation
* Recreated workflow diagrams

---

## 🚫 Out of Scope

This repository will not include:

* Real MLS exports
* Real agent names
* Real agent emails
* Real phone numbers
* Real property addresses
* Real listing IDs
* Real brokerage contact lists
* Real Gmail messages
* Internal Google Sheets
* Apps Script deployment URLs
* Tracking pixel URLs
* Internal company screenshots
* Any confidential Westside Property Management data

---

## 🏗️ Data Architecture Requirements

The project will use a medallion-style data workflow.

| Layer     | Folder                | Requirement                                    |
| --------- | --------------------- | ---------------------------------------------- |
| Bronze    | `datasets/raw/`       | Store synthetic raw MLS-style listing exports  |
| Silver    | `datasets/cleaned/`   | Store cleaned and standardized listing records |
| Gold      | `outputs/`            | Store campaign-ready outreach queue outputs    |
| Analytics | `datasets/analytics/` | Store campaign summary and performance metrics |

---

## 🥉 Bronze Layer Requirements

The raw layer must contain synthetic listing files that represent original MLS-style exports.

Required raw fields:

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

The raw files should intentionally include some realistic data quality issues, such as missing emails, inconsistent phone formatting, mixed city casing, and duplicate contact records.

---

## 🥈 Silver Layer Requirements

The cleaned layer must standardize raw listing data into a consistent structure.

Required cleaning rules:

* Standardize column names to snake_case.
* Trim extra spaces from all text fields.
* Normalize city names.
* Normalize phone numbers to 10-digit format when possible.
* Validate email format.
* Split agent full name into first and last name fields.
* Create listing age fields.
* Create price bands.
* Flag missing email and phone fields.
* Flag duplicate agent or listing records.
* Assign QA status.

---

## 🥇 Gold Layer Requirements

The gold layer must create a campaign-ready outreach queue.

Required campaign queue fields:

* lead_id
* campaign_type
* listing_status
* agent_first_name
* agent_last_name
* agent_email_clean
* agent_phone_clean
* brokerage_clean
* city_cluster
* price_band
* listing_age_days
* outreach_priority
* email_available
* phone_available
* qa_status
* send_status
* follow_up_status

---

## 📊 Analytics Requirements

The analytics layer must summarize campaign readiness and outreach performance.

Required summary metrics:

* total_leads
* valid_email_count
* missing_email_count
* valid_phone_count
* missing_phone_count
* duplicate_count
* qa_pass_count
* qa_fail_count
* qa_pass_rate
* high_priority_count
* sent_count
* opened_count
* clicked_count
* replied_count
* follow_up_required_count

---

## 🧪 Data Quality Requirements

The project must include validation checks for:

* Missing required fields
* Invalid email format
* Invalid phone format
* Duplicate listing IDs
* Duplicate agent contact records
* Missing campaign type
* Missing listing status
* Missing city
* Missing price band
* Invalid QA status
* Invalid outreach priority

---

## ⚙️ Automation Logic Requirements

The automation logic should represent how campaign tracking works after a lead enters the outreach queue.

Tracking fields should include:

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

The public repository may include Apps Script-style pseudocode to explain outreach tracking without exposing real deployment code.

---

## 📁 Documentation Requirements

The `docs/` folder should include:

* `requirements.md`
* `data_architecture.md`
* `data_catalog.md`
* `pipeline_workflow.md`
* `qa_rules.md`
* `automation_logic.md`
* `naming_conventions.md`

---

## 🛠️ Script Requirements

The `scripts/` folder should include:

* `scripts/bronze/01_load_raw_mls_exports.py`
* `scripts/silver/02_clean_and_standardize_leads.py`
* `scripts/gold/03_build_campaign_queue.py`
* `scripts/analytics/04_generate_campaign_summary.py`

---

## 🧾 Testing Requirements

The `tests/` folder should include data quality checks that validate whether the generated files meet the project rules.

Example test file:

* `tests/test_data_quality_rules.py`

---

## 🔒 Confidentiality Requirements

All files in this repository must be public-safe.

No real company, MLS, agent, owner, tenant, property, Gmail, Google Sheets, or Apps Script data should be uploaded.

Only synthetic records, generalized logic, recreated diagrams, and public-safe documentation should be used.

---

## ✅ Success Criteria

The project is complete when it includes:

* A professional README
* Synthetic raw listing data
* Cleaned output data
* Campaign queue output
* Campaign analytics output
* Python scripts for the full workflow
* QA validation tests
* Documentation files
* Recreated diagrams
* Clear confidentiality notice
* Resume-ready and LinkedIn-ready project positioning
