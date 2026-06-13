# 🏡 Luxury Rental Lead Pipeline & MLS Outreach Automation System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-lightgrey)
![Pytest](https://img.shields.io/badge/Pytest-Data%20Quality-green)
![Status](https://img.shields.io/badge/Status-Portfolio%20Project-orange)
![Data](https://img.shields.io/badge/Data-Synthetic%20Only-red)

A portfolio-grade data automation and growth operations project based on a real luxury rental lead workflow.

This project shows how raw MLS-style luxury rental listing files can be converted into a structured lead pipeline for high-value property management growth. The workflow covers data ingestion, cleaning, standardization, lead segmentation, campaign queue preparation, outreach tracking logic, and analytics-ready reporting.

This repository is a public-safe reconstruction. All sample data is synthetic. No confidential company data, real MLS records, agent contact information, property addresses, internal Google Sheets, internal email messages, Apps Script deployment links, or private company files are included.

---

## 👤 Recruiter Summary

This project demonstrates my ability to turn a messy business-development workflow into a structured data and automation system.

I designed a synthetic MLS-style lead pipeline that takes raw luxury rental listing exports, cleans and validates the data, flags records that need review, builds a campaign-ready outreach queue, and produces analytics-ready summary metrics.

The project connects technical execution with marketing operations: Python, pandas, QA validation, campaign workflow design, automation logic, and performance reporting.

All files are public-safe and use synthetic data only.

---

## 🧩 Portfolio Positioning

This project is positioned as a technical marketing operations and data workflow project.

It is not only a campaign example. It shows how a business-development process can be redesigned into a structured operating system with:

* Defined data layers
* Repeatable cleaning rules
* QA validation
* Campaign queue logic
* Outreach readiness tracking
* Reporting outputs
* Public-safe documentation

The project is designed to show practical experience across data analysis, marketing operations, automation planning, and workflow architecture.

---

## 📊 Project Metrics Snapshot

The synthetic dataset and outputs demonstrate the full workflow from raw data to campaign reporting.

| Metric                           | Value |
| -------------------------------- | ----: |
| Synthetic raw listing records    |    25 |
| Cleaned lead records             |    25 |
| Campaign queue records           |    25 |
| QA pass records                  |    18 |
| QA review records                |     6 |
| QA fail records                  |     1 |
| QA pass rate                     |   72% |
| High-priority outreach records   |     9 |
| Medium-priority outreach records |     9 |
| Review-priority records          |     6 |
| Low-priority records             |     1 |
| Valid email readiness rate       |   92% |
| Valid phone readiness rate       |   92% |
| Duplicate listing ID rate        |    8% |
| Outreach-ready rate              |   72% |

---

## ✨ Project Highlights

* Built a medallion-style data workflow using Bronze, Silver, Gold, and Analytics layers.
* Converted raw MLS-style luxury rental listing data into cleaned and standardized lead records.
* Designed QA rules for missing fields, invalid emails, invalid phones, duplicate listing IDs, and review records.
* Created a campaign-ready outreach queue with lead IDs, campaign types, outreach priority, send status, and follow-up status.
* Added Python scripts for raw data profiling, cleaning, campaign queue generation, and analytics reporting.
* Added pytest-style validation checks to confirm output structure and summary accuracy.
* Documented the workflow with requirements, data architecture, data catalog, QA rules, automation logic, visual architecture, and a case study.
* Used only synthetic data and public-safe documentation.

---

## 📈 Business Impact

This project shows how a manual lead-preparation workflow can be converted into a repeatable data and automation system.

The pipeline improves the workflow by:

* Turning raw listing exports into structured lead records.
* Reducing manual cleanup through standardized cleaning rules.
* Separating campaign-ready records from records that need review.
* Creating clear QA logic for missing fields, invalid contact data, duplicate listings, and incomplete records.
* Supporting more consistent outreach execution through campaign-ready queues.
* Making campaign readiness visible through analytics metrics.
* Connecting marketing operations, data quality, automation logic, and reporting in one workflow.

The main value is not only outreach execution. The value is building a cleaner operating system for luxury rental lead generation.

---

## 🎯 Project Objective

The objective of this project is to demonstrate how a raw listing-data workflow can be turned into a repeatable growth system.

Instead of treating luxury rental outreach as a manual spreadsheet task, the system is structured like a data pipeline:

```text
Raw MLS-style listing files
        ↓
Cleaned and standardized lead records
        ↓
Validated campaign-ready outreach queue
        ↓
Automated outreach tracking logic
        ↓
Campaign summary and performance reporting
```

---

## 💼 Business Problem

Luxury rental listings can reveal high-value opportunities for property management outreach, agent referrals, and owner lead generation.

The challenge is that raw listing exports are not immediately ready for campaign execution. They often require cleaning, field standardization, QA checks, segmentation, and tracking fields before they can support repeatable outreach.

Common issues include:

* Inconsistent listing fields
* Missing or inconsistent agent contact data
* Different formats for names, phones, emails, dates, cities, and listing prices
* New listing and leased listing records mixed across separate workflows
* No standardized campaign queue
* No clean tracking structure for sent, opened, clicked, replied, or follow-up status
* Limited visibility into campaign readiness and outreach performance

---

## 👩‍💻 My Role

I worked on structuring the workflow from raw listing data into campaign-ready lead tracking.

My responsibilities included:

* Cleaning raw luxury rental listing exports
* Standardizing listing, agent, and campaign fields
* Separating new-listing and leased-property opportunities
* Preparing outreach-ready tracker structures
* Supporting automation logic for batched sending and follow-up tracking
* Building a repeatable workflow that could support lead generation, agent referral development, and campaign reporting
* Documenting the workflow in a public-safe way using synthetic data only

---

## 🏗️ Data Architecture

This public version uses a medallion-style data architecture.

📌 View the full visual workflow here: [`docs/project_architecture.md`](docs/project_architecture.md)

| Layer        | Folder                | Purpose                                              |
| ------------ | --------------------- | ---------------------------------------------------- |
| 🥉 Bronze    | `datasets/raw/`       | Synthetic raw MLS-style listing exports              |
| 🥈 Silver    | `datasets/cleaned/`   | Cleaned and standardized listing and contact records |
| 🥇 Gold      | `outputs/`            | Campaign-ready outreach queue and reporting outputs  |
| 📊 Analytics | `datasets/analytics/` | Campaign summary and performance metrics             |

---

## 🔄 Pipeline Workflow

### 1. 🥉 Bronze Layer: Raw Listing Data

The raw layer represents MLS-style listing exports before cleaning.

Example fields:

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

### 2. 🥈 Silver Layer: Cleaned Lead Records

The silver layer standardizes fields and prepares records for QA.

Cleaning steps include:

* Standardizing column names
* Cleaning agent first and last names
* Normalizing phone numbers
* Validating email format
* Standardizing city names
* Creating listing age fields
* Creating price bands
* Flagging missing contact fields
* Assigning QA status

### 3. 🥇 Gold Layer: Campaign Queue

The gold layer creates an outreach-ready campaign queue.

Campaign fields include:

* lead_id
* campaign_type
* agent_first_name
* city_cluster
* price_band
* listing_status
* outreach_priority
* email_available
* phone_available
* qa_status
* send_status
* follow_up_status

### 4. 📊 Analytics Layer: Campaign Reporting

The analytics layer summarizes campaign readiness and outreach performance.

Example metrics:

* total leads
* emails available
* missing email count
* QA pass rate
* sent count
* open count
* click count
* reply count
* follow-up count

---

## 📘 Case Study

This project includes a full public-safe case study explaining the business problem, pipeline design, automation logic, QA rules, and reporting structure.

📌 Read the case study here: [`docs/case_study.md`](docs/case_study.md)

---

## 📂 Repository Structure

```text
luxury-rental-mls-outreach-pipeline/
│
├── datasets/
│   ├── raw/                  # Synthetic raw MLS-style exports
│   ├── cleaned/              # Cleaned and standardized mock data
│   └── analytics/            # Mock campaign summary data
│
├── docs/
│   ├── requirements.md
│   ├── data_architecture.md
│   ├── data_catalog.md
│   ├── pipeline_workflow.md
│   ├── qa_rules.md
│   ├── automation_logic.md
│   ├── naming_conventions.md
│   ├── project_architecture.md
│   └── case_study.md
│
├── scripts/
│   ├── bronze/               # Raw data loading scripts
│   ├── silver/               # Cleaning and standardization scripts
│   ├── gold/                 # Campaign queue generation scripts
│   └── analytics/            # Campaign reporting scripts
│
├── tests/                    # Data quality and validation checks
├── images/                   # Recreated diagrams and mock visuals
├── outputs/                  # Generated public-safe outputs
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🚀 How to Run This Project

This project uses synthetic data only. No real company, MLS, agent, property, email, or internal system data is included.

### 1. Clone the Repository

```bash
git clone https://github.com/AnoohyaAlluri/luxury-rental-mls-outreach-pipeline.git
cd luxury-rental-mls-outreach-pipeline
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

For macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. Run the Full Pipeline

```bash
python run_pipeline.py
```

This runs the pipeline in order:

```text
Bronze Layer: raw data validation and profiling
        ↓
Silver Layer: data cleaning and standardization
        ↓
Gold Layer: campaign queue generation
        ↓
Analytics Layer: campaign summary reporting
```

### 6. Run Data Quality Tests

```bash
pytest
```

---

## 📤 Generated Outputs

After the pipeline runs, it creates these public-safe synthetic outputs:

| Output               | Location                                            | Purpose                                  |
| -------------------- | --------------------------------------------------- | ---------------------------------------- |
| Raw data profile     | `datasets/analytics/raw_data_profile_mock.csv`      | Summarizes raw synthetic listing quality |
| Cleaned lead records | `datasets/cleaned/cleaned_luxury_listing_leads.csv` | Standardized listing and contact fields  |
| Campaign queue       | `outputs/campaign_queue_mock.csv`                   | Outreach-ready lead queue                |
| Campaign summary     | `datasets/analytics/campaign_summary_mock.csv`      | Campaign readiness and reporting metrics |

---

## ⚙️ Technical Components

This repository includes:

* Synthetic CSV datasets
* Python scripts for data cleaning and validation
* Campaign queue generation logic
* Data quality checks
* Campaign reporting outputs
* Apps Script-style pseudocode for outreach tracking
* Mermaid-based workflow diagrams
* Public-safe documentation for business logic and QA rules

---

## 🛠️ Tools Represented

The original workflow involved a marketing operations stack. This public reconstruction represents the workflow using safe, general tools:

* Google Sheets-style tracker logic
* Google Apps Script-style automation logic
* Email-style outreach tracking concepts
* MLS-style listing exports
* Python for public-safe data pipeline reconstruction
* CSV-based mock data
* QA rules and reporting logic
* GitHub documentation

---

## 🎯 How This Project Maps to Real Roles

| Target Role                  | How This Project Supports It                                                                               |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Marketing Analyst            | Shows campaign data preparation, lead segmentation, reporting metrics, and performance-readiness analysis  |
| Growth Marketing Analyst     | Connects raw lead signals to campaign execution, prioritization, and follow-up workflows                   |
| Data Analyst                 | Demonstrates data cleaning, QA validation, summary reporting, and structured CSV-based analytics           |
| Marketing Operations Analyst | Shows how manual outreach preparation can be converted into a repeatable operating workflow                |
| Revenue Operations Analyst   | Demonstrates lead pipeline structure, status tracking, quality control, and campaign handoff logic         |
| Automation Specialist        | Documents automation logic for batching, send status, engagement tracking, and follow-up workflows         |
| Technical Marketing Analyst  | Combines Python, pandas, campaign strategy, QA rules, and analytics reporting in one project               |
| AI / Data Workflow Builder   | Shows how business-development workflows can be structured for future automation or AI-assisted operations |

---

## 🧠 Technical Skills Matrix

| Skill Area           | What This Project Demonstrates                                                                                        |
| -------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Data Cleaning        | Standardizes raw MLS-style listing fields, agent names, cities, property types, emails, and phone numbers             |
| Data Validation      | Flags missing fields, invalid emails, invalid phones, duplicate listing IDs, and records needing review               |
| Pipeline Design      | Uses Bronze, Silver, Gold, and Analytics layers to structure the workflow                                             |
| Python               | Uses Python scripts to load, clean, transform, and summarize synthetic data                                           |
| pandas               | Uses pandas for CSV processing, field transformation, QA logic, and summary reporting                                 |
| Testing              | Uses pytest-style checks to validate required columns, status values, and summary totals                              |
| Marketing Operations | Converts raw listing data into campaign-ready outreach queues                                                         |
| Campaign Analytics   | Produces readiness metrics, QA pass rates, priority counts, and outreach summary fields                               |
| Automation Logic     | Documents batched sending, open tracking, click tracking, reply tracking, and follow-up logic                         |
| Documentation        | Includes requirements, data catalog, architecture, workflow, QA rules, automation logic, and case study documentation |
| Confidentiality      | Uses synthetic data and public-safe examples only                                                                     |

---

## 📌 Key Skills Demonstrated

* Data cleaning
* Data validation
* Lead pipeline design
* Marketing operations analytics
* Campaign queue generation
* Outreach automation logic
* QA rule design
* Synthetic data modeling
* Workflow documentation
* Growth operations reporting
* Confidentiality-safe portfolio presentation

---

## 🔒 Confidentiality Notice

This repository is a public-safe reconstruction of a real growth operations workflow I worked on for a property management company.

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
* Any confidential company data

All records, examples, files, and outputs are synthetic or generalized for portfolio demonstration.

---

## 🚧 Status

This repository is a completed public-safe portfolio reconstruction of a luxury rental lead pipeline and outreach automation workflow.

Completed build phases:

1. Created project structure
2. Added synthetic raw listing dataset
3. Built data cleaning scripts
4. Built campaign queue generation logic
5. Added QA validation checks
6. Added analytics summary outputs
7. Added workflow diagrams
8. Added public-safe case study
9. Finalized portfolio-facing documentation

---

## 🌱 About This Project

This project is designed to show how marketing operations work can be structured like a technical data system.

The goal is to demonstrate that growth work is not only campaign execution. It can include data architecture, QA logic, automation design, reporting workflows, and business development systems.
