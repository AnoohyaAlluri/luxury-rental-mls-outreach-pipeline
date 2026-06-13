# 🏡 Luxury Rental Lead Pipeline & MLS Outreach Automation System

A portfolio-grade data automation and growth operations project based on a real luxury rental lead workflow.

This project shows how raw MLS-style luxury rental listing files can be converted into a structured lead pipeline for high-value property management growth. The workflow covers data ingestion, cleaning, standardization, lead segmentation, campaign queue preparation, outreach tracking logic, and analytics-ready reporting.

This repository is a public-safe reconstruction. All sample data is synthetic. No confidential company data, real MLS records, agent contact information, property addresses, internal Google Sheets, internal email messages, Apps Script deployment links, or private company files are included.

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
│   └── naming_conventions.md
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

This repository will include:

* Synthetic CSV datasets
* Python scripts for data cleaning and validation
* Campaign queue generation logic
* Data quality checks
* Campaign reporting outputs
* Apps Script-style pseudocode for outreach tracking
* Recreated diagrams for pipeline architecture and workflow design
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

This repository is being built as a professional portfolio project.

Planned build phases:

1. Create project structure
2. Add synthetic raw listing datasets
3. Build data cleaning scripts
4. Build campaign queue generation logic
5. Add QA validation checks
6. Add analytics summary outputs
7. Add workflow diagrams
8. Finalize documentation and portfolio case study

---

## 🌱 About This Project

This project is designed to show how marketing operations work can be structured like a technical data system.

The goal is to demonstrate that growth work is not only campaign execution. It can include data architecture, QA logic, automation design, reporting workflows, and business development systems.
