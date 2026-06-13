# 🧭 Project Architecture Diagram

## Overview

This diagram shows how the **Luxury Rental Lead Pipeline & MLS Outreach Automation System** moves data from raw MLS-style listing files into cleaned lead records, campaign-ready outreach queues, and analytics outputs.

All data represented in this project is synthetic and public-safe.

---

## 🏗️ End-to-End Architecture

```mermaid
flowchart TD
    A["🥉 Bronze Layer<br/>Raw MLS-style listing exports<br/>datasets/raw/"] 
    --> B["Raw Data Validation<br/>Required columns<br/>Blank field checks<br/>Duplicate listing ID checks"]

    B --> C["🥈 Silver Layer<br/>Cleaned lead records<br/>datasets/cleaned/"]

    C --> D["Data Cleaning Logic<br/>Normalize cities<br/>Clean agent names<br/>Validate emails<br/>Normalize phones<br/>Create price bands<br/>Assign QA status"]

    D --> E["🥇 Gold Layer<br/>Campaign-ready outreach queue<br/>outputs/"]

    E --> F["Campaign Logic<br/>Assign campaign type<br/>Assign outreach priority<br/>Initialize send status<br/>Initialize follow-up status"]

    F --> G["📊 Analytics Layer<br/>Campaign summary metrics<br/>datasets/analytics/"]

    G --> H["Reporting Outputs<br/>Email readiness<br/>Phone readiness<br/>QA pass rate<br/>Priority counts<br/>Outreach readiness rate"]
```

---

## 🔄 Pipeline Execution Order

```mermaid
flowchart LR
    A["01 Load Raw MLS Exports"] 
    --> B["02 Clean and Standardize Leads"] 
    --> C["03 Build Campaign Queue"] 
    --> D["04 Generate Campaign Summary"] 
    --> E["Run Data Quality Tests"]
```

---

## 🧪 QA Workflow

```mermaid
flowchart TD
    A["Raw Listing Record"] --> B{"Required Fields Present?"}
    B -- No --> C["FAIL<br/>Missing required data"]
    B -- Yes --> D{"Valid Email or Phone?"}
    D -- No --> C
    D -- Yes --> E{"Duplicate Listing ID?"}
    E -- Yes --> F["REVIEW<br/>Duplicate risk"]
    E -- No --> G{"Price and City Valid?"}
    G -- No --> F
    G -- Yes --> H["PASS<br/>Campaign-ready record"]
```

---

## 📬 Outreach Tracking Workflow

```mermaid
flowchart TD
    A["Not Sent"] --> B["Sent"]
    B --> C["Opened"]
    C --> D["Clicked"]
    D --> E["Replied"]

    B --> F["No Reply After Follow-Up Window"]
    F --> G["Follow-up Required"]
    G --> H["Follow-up Sent"]
    H --> I["Completed"]
```

---

## 📌 Architecture Summary

| Layer     | Main Purpose                                             | Output                    |
| --------- | -------------------------------------------------------- | ------------------------- |
| Bronze    | Validate raw synthetic listing files                     | Raw data profile          |
| Silver    | Clean and standardize listing, agent, and contact fields | Cleaned lead records      |
| Gold      | Build campaign-ready outreach queue                      | Prioritized outreach file |
| Analytics | Summarize readiness and performance metrics              | Campaign summary          |
| Tests     | Validate output quality                                  | QA test results           |

---

## 🔒 Confidentiality Note

This architecture is a public-safe reconstruction. It does not include real company files, MLS exports, agent contact data, property addresses, internal Google Sheets, internal email messages, deployment links, tracking URLs, or screenshots from private systems.
