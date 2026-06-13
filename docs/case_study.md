# 📘 Case Study: Luxury Rental Lead Pipeline & MLS Outreach Automation System

## Overview

This case study explains a public-safe reconstruction of a real growth operations workflow.

The project demonstrates how raw MLS-style luxury rental listing files can be transformed into a structured lead pipeline for property management growth. The system uses synthetic data to show data cleaning, QA validation, campaign queue generation, outreach tracking logic, and analytics-ready reporting.

No real company data, MLS records, agent contact details, property addresses, internal email messages, private spreadsheets, deployment links, or screenshots are included.

---

## Business Context

Luxury rental listings can create valuable opportunities for property management outreach.

When a high-value rental property is newly listed or recently leased, it may signal a potential opportunity for:

* Agent referral development
* Owner lead generation
* Luxury rental pipeline tracking
* Follow-up outreach
* Campaign performance analysis

The original workflow required turning raw listing files into a cleaner, repeatable system that could support outreach and reporting.

---

## Problem

Raw listing exports are not automatically ready for marketing or business development.

The workflow had several operational problems:

* Listing files needed cleaning before outreach.
* Agent and contact fields needed standardization.
* New-listing and leased-property opportunities required different handling.
* Some records had missing or invalid email or phone data.
* Duplicate records needed to be flagged.
* Outreach needed a consistent tracker structure.
* Campaign performance needed summary metrics.
* Sensitive company and contact data could not be exposed publicly.

---

## Solution

I structured the workflow as a data pipeline with four layers:

```text
Bronze Layer
Raw synthetic MLS-style listing exports

        ↓

Silver Layer
Cleaned and standardized lead records

        ↓

Gold Layer
Campaign-ready outreach queue

        ↓

Analytics Layer
Campaign readiness and performance reporting
```

This structure turns a manual lead-preparation workflow into a repeatable data and automation system.

---

## My Role

My work focused on transforming raw listing data into campaign-ready lead tracking.

Responsibilities included:

* Cleaning raw luxury rental listing exports
* Standardizing listing, agent, and contact fields
* Separating new-listing and leased-property opportunities
* Creating campaign-ready tracker structures
* Supporting batched outreach and follow-up tracking logic
* Defining QA rules for missing fields, invalid contacts, duplicates, and review records
* Structuring reporting outputs for campaign readiness and performance analysis
* Rebuilding the project publicly with synthetic data only

---

## Technical Workflow

### 1. Raw Data Intake

The Bronze Layer stores synthetic raw listing exports.

The raw data includes fields such as:

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

The raw file intentionally includes data quality issues so the pipeline can demonstrate cleaning and validation.

---

### 2. Data Cleaning and Standardization

The Silver Layer cleans and standardizes the raw data.

Cleaning logic includes:

* Converting column names to snake_case
* Trimming extra spaces
* Standardizing city names
* Mapping property types
* Normalizing phone numbers
* Validating email format
* Splitting agent full names into first and last name
* Creating listing age fields
* Creating price bands
* Flagging duplicate listing IDs
* Assigning QA status

---

### 3. Campaign Queue Generation

The Gold Layer converts cleaned records into an outreach-ready campaign queue.

The campaign queue includes:

* lead_id
* campaign_type
* campaign status
* agent first name
* cleaned contact fields
* city cluster
* price band
* outreach priority
* QA status
* send status
* follow-up status

This gives the workflow a clear handoff point between data preparation and campaign execution.

---

### 4. Automation Logic

The project includes public-safe automation logic for outreach tracking.

The automation structure represents:

* Batched sending logic
* Message ID tracking
* Send status updates
* Open tracking concepts
* Click tracking concepts
* Reply tracking concepts
* Follow-up status updates
* Final outcome classification

The repository does not include real Apps Script code, real email threads, deployment URLs, tracking pixels, or private execution logs.

---

### 5. Analytics and Reporting

The Analytics Layer summarizes campaign readiness and performance.

Example metrics include:

* total leads
* valid email count
* missing email count
* valid phone count
* missing phone count
* duplicate count
* QA pass rate
* high-priority lead count
* outreach-ready count
* send, open, click, and reply counts

These metrics help show whether the campaign queue is ready for outreach and where data quality issues remain.

---

## Data Quality Rules

The project includes QA logic for:

* Required column validation
* Missing listing IDs
* Missing listing status
* Invalid email format
* Invalid phone format
* Missing city
* Missing listing price
* Missing agent name
* Duplicate listing IDs
* Invalid campaign type
* Invalid outreach priority
* Summary count reconciliation

Each record is classified as:

| QA Status | Meaning                                                    |
| --------- | ---------------------------------------------------------- |
| PASS      | Record is campaign-ready                                   |
| REVIEW    | Record needs manual review before outreach                 |
| FAIL      | Record should not be used for outreach in its current form |

---

## Public-Safe Outputs

The repository includes synthetic outputs only:

| Output                             | Purpose                                    |
| ---------------------------------- | ------------------------------------------ |
| `raw_data_profile_mock.csv`        | Raw file quality summary                   |
| `cleaned_luxury_listing_leads.csv` | Cleaned and standardized lead records      |
| `campaign_queue_mock.csv`          | Outreach-ready campaign queue              |
| `campaign_summary_mock.csv`        | Campaign readiness and performance summary |

---

## Skills Demonstrated

This project demonstrates:

* Data cleaning
* Data validation
* Pipeline architecture
* Campaign queue design
* QA rule design
* Marketing operations analytics
* Outreach automation logic
* Synthetic data modeling
* Python scripting
* pandas workflows
* pytest-style validation
* Technical documentation
* Confidentiality-safe portfolio presentation

---

## Business Impact Framing

This project shows how a marketing operations workflow can be structured like a technical data system.

The value of the workflow is that it helps convert raw listing data into a cleaner and more repeatable lead-generation process. Instead of relying only on manual spreadsheet handling, the system creates a clear path from raw data to campaign readiness, automation logic, and reporting.

---

## Confidentiality Notice

This case study is a public-safe reconstruction.

It does not include:

* Real MLS exports
* Real agent names
* Real emails
* Real phone numbers
* Real brokerage contact lists
* Real property addresses
* Real listing IDs
* Real listing prices tied to actual properties
* Internal Google Sheets
* Internal email messages
* Apps Script deployment URLs
* Tracking pixel URLs
* Internal execution logs
* Screenshots from company systems
* Raw Drive documents
* Confidential company data

All records, examples, files, and outputs are synthetic or generalized for portfolio demonstration.

---

## Summary

This project demonstrates how growth operations work can be presented as a technical system.

It combines data cleaning, campaign operations, automation logic, QA validation, and analytics reporting into one public-safe portfolio project.
