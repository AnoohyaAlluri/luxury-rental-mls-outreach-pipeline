# 🧪 QA Rules

## Overview

This document defines the data quality rules for the **Luxury Rental Lead Pipeline & MLS Outreach Automation System**.

The goal of the QA layer is to make sure raw listing records are cleaned, validated, and prepared correctly before they enter the campaign queue.

This project uses synthetic data only. The QA logic represents the workflow structure without exposing real MLS, agent, property, company, or outreach data.

---

## 🎯 QA Objectives

The QA process is designed to:

* Identify missing required fields
* Standardize inconsistent listing and contact data
* Flag invalid emails and phone numbers
* Detect duplicate records
* Separate campaign-ready records from records needing review
* Prevent incomplete or low-quality records from entering outreach
* Create clear audit notes for each record

---

## 🥉 Bronze Layer QA

The Bronze Layer checks whether the raw MLS-style export has the minimum required structure.

### Required Fields

The raw input file must include:

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

### Bronze QA Rules

| Rule ID | Rule                   | Pass Condition                   | Fail Condition                           |
| ------- | ---------------------- | -------------------------------- | ---------------------------------------- |
| B001    | Required columns exist | All required columns are present | One or more required columns are missing |
| B002    | Listing ID exists      | `listing_id` is not blank        | `listing_id` is blank                    |
| B003    | Listing status exists  | `listing_status` is not blank    | `listing_status` is blank                |
| B004    | Source file exists     | `source_file` is not blank       | `source_file` is blank                   |
| B005    | Listing date exists    | `listing_date` is not blank      | `listing_date` is blank                  |

---

## 🥈 Silver Layer QA

The Silver Layer validates cleaned and standardized lead records.

### Email QA

| Rule ID | Rule                  | Pass Condition                          | Review or Fail Condition                 |
| ------- | --------------------- | --------------------------------------- | ---------------------------------------- |
| S001    | Email exists          | Email field is not blank                | Blank email is flagged                   |
| S002    | Email format is valid | Email contains `@` and a domain pattern | Invalid format is flagged                |
| S003    | Email is standardized | Email is lowercase and trimmed          | Extra spaces or mixed casing are cleaned |

### Phone QA

| Rule ID | Rule                  | Pass Condition                            | Review or Fail Condition                         |
| ------- | --------------------- | ----------------------------------------- | ------------------------------------------------ |
| S004    | Phone exists          | Phone field is not blank                  | Blank phone is flagged                           |
| S005    | Phone is normalized   | Phone resolves to 10 digits               | Invalid phone is flagged                         |
| S006    | Phone format is clean | Phone contains digits only after cleaning | Symbols or partial values are removed or flagged |

### Listing QA

| Rule ID | Rule                          | Pass Condition                        | Review or Fail Condition                   |
| ------- | ----------------------------- | ------------------------------------- | ------------------------------------------ |
| S007    | City is standardized          | City is mapped to a clean value       | Unknown city is flagged                    |
| S008    | Property type is standardized | Property type maps to accepted values | Unknown property type is flagged           |
| S009    | Listing price is valid        | Price is numeric and greater than 0   | Missing or invalid price is flagged        |
| S010    | Price band is assigned        | Price maps to a defined band          | Missing price band is flagged              |
| S011    | Listing age is calculated     | Listing age field is populated        | Missing or invalid listing date is flagged |

### Agent QA

| Rule ID | Rule                    | Pass Condition           | Review or Fail Condition      |
| ------- | ----------------------- | ------------------------ | ----------------------------- |
| S012    | Agent name exists       | Agent name is not blank  | Blank agent name is flagged   |
| S013    | Agent first name exists | First name can be parsed | Missing first name is flagged |
| S014    | Brokerage exists        | Brokerage is not blank   | Blank brokerage is flagged    |

### Duplicate QA

| Rule ID | Rule                     | Pass Condition                                             | Review or Fail Condition                    |
| ------- | ------------------------ | ---------------------------------------------------------- | ------------------------------------------- |
| S015    | Duplicate listing check  | Listing ID appears once                                    | Repeated listing ID is flagged              |
| S016    | Duplicate contact check  | Same agent email and phone are not repeated excessively    | Repeated contact data is flagged for review |
| S017    | Duplicate campaign check | Same listing is not assigned to duplicate active campaigns | Duplicate outreach risk is flagged          |

---

## 🥇 Gold Layer QA

The Gold Layer validates that records are ready for outreach.

### Campaign Queue QA

| Rule ID | Rule                         | Pass Condition                                       | Review or Fail Condition                    |
| ------- | ---------------------------- | ---------------------------------------------------- | ------------------------------------------- |
| G001    | Lead ID exists               | `lead_id` is populated                               | Missing lead ID is flagged                  |
| G002    | Campaign type exists         | Campaign type is New Listing or Leased Follow-up     | Missing or invalid campaign type is flagged |
| G003    | Outreach priority exists     | Priority is High, Medium, Low, or Review             | Missing priority is flagged                 |
| G004    | QA status exists             | QA status is PASS, REVIEW, or FAIL                   | Missing QA status is flagged                |
| G005    | Send status initialized      | Send status begins as Not Sent                       | Missing send status is flagged              |
| G006    | Follow-up status initialized | Follow-up status begins as Not Started or Not Needed | Missing follow-up status is flagged         |

---

## 📊 Analytics QA

The Analytics Layer checks whether summary numbers are traceable to the campaign queue.

| Rule ID | Rule                                   | Pass Condition                                                | Fail Condition                   |
| ------- | -------------------------------------- | ------------------------------------------------------------- | -------------------------------- |
| A001    | Total lead count matches               | Summary total equals campaign queue row count                 | Counts do not match              |
| A002    | Email counts reconcile                 | Valid email plus missing email equals total leads             | Counts do not reconcile          |
| A003    | QA counts reconcile                    | PASS plus REVIEW plus FAIL equals total leads                 | Counts do not reconcile          |
| A004    | QA pass rate is valid                  | QA pass rate is between 0 and 100                             | Invalid percentage               |
| A005    | Engagement counts are not negative     | Sent, opened, clicked, and replied counts are zero or greater | Negative values                  |
| A006    | Reply count does not exceed sent count | Replied count is less than or equal to sent count             | Replied count exceeds sent count |

---

## 🚦 QA Status Logic

Each record receives one QA status.

| QA Status | Meaning                                                                    |
| --------- | -------------------------------------------------------------------------- |
| PASS      | Record is campaign-ready                                                   |
| REVIEW    | Record has missing or uncertain information but may be usable after review |
| FAIL      | Record should not be used for outreach in its current form                 |

### PASS Example

A record can pass QA when:

* Listing ID is present
* Listing status is valid
* City is standardized
* Price band is assigned
* Agent name is present
* Email is valid
* Campaign type is assigned
* Outreach priority is assigned

### REVIEW Example

A record should be reviewed when:

* Phone is missing but email is valid
* Email is missing but phone is valid
* Brokerage is missing
* City needs manual confirmation
* Duplicate contact signal exists
* Listing date is unclear

### FAIL Example

A record should fail QA when:

* Listing ID is missing
* Agent name is missing
* Both email and phone are missing
* Listing status is missing
* Campaign type cannot be assigned
* Record appears duplicated and unsafe for outreach

---

## 🧭 Outreach Priority Logic

Outreach priority helps segment records before campaign execution.

| Priority | Example Logic                                                   |
| -------- | --------------------------------------------------------------- |
| High     | Valid email, target city cluster, high price band, QA PASS      |
| Medium   | Valid email, target city cluster, moderate price band, QA PASS  |
| Review   | Some useful data exists, but record needs manual review         |
| Low      | Record is outside target criteria or has weak contact readiness |

---

## 🧾 Example QA Notes

Public-safe QA notes should explain the issue without exposing private data.

Examples:

* `Valid email and phone`
* `Missing phone, email available`
* `Invalid email format`
* `Duplicate listing ID`
* `Needs city review`
* `Missing campaign type`
* `Both email and phone missing`
* `Excluded from campaign queue`

---

## 🔒 Confidentiality Rule

QA files must never include real company data, real MLS exports, real agent names, real emails, real phone numbers, real property addresses, real listing IDs, real Gmail details, internal Google Sheets, tracking URLs, or Apps Script deployment links.

All QA examples must use synthetic records only.
