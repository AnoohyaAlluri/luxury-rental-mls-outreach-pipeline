# ⚙️ Automation Logic

## Overview

This document explains the automation logic behind the **Luxury Rental Lead Pipeline & MLS Outreach Automation System**.

The goal is to show how cleaned luxury rental listing records can move from a campaign-ready queue into an outreach tracking workflow.

This file uses public-safe pseudocode and generalized automation concepts only. It does not include real Apps Script code, Gmail threads, deployment links, tracking URLs, message IDs, or company data.

---

## 🎯 Automation Objective

The automation layer is designed to support:

* Batched outreach sending
* Message ID tracking
* Send status updates
* Open tracking logic
* Click tracking logic
* Reply tracking logic
* Follow-up status updates
* Final outcome classification
* Campaign reporting

---

## 🔄 Outreach Status Flow

Each lead moves through a structured campaign lifecycle.

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

Some records may also move through a follow-up path:

```text
No Reply
   ↓
Follow-up Required
   ↓
Follow-up Sent
   ↓
Completed
```

---

## 📥 Input Table

The automation layer starts with the campaign queue.

```text
outputs/campaign_queue_mock.csv
```

Required input fields:

* lead_id
* campaign_type
* agent_first_name
* agent_email_clean
* city_cluster
* price_band
* outreach_priority
* qa_status
* send_status
* follow_up_status

Only records with `qa_status = PASS` should enter the active outreach queue.

---

## 📤 Output Tracking Fields

The automation workflow updates tracking fields such as:

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

---

## 🧱 Batch Sending Logic

The sending workflow should process a controlled number of records per run.

### Purpose

Batching prevents the workflow from sending too many messages at once and makes the system easier to monitor.

### Pseudocode

```text
FOR each lead in campaign_queue:
    IF qa_status = "PASS"
    AND send_status = "Not Sent"
    AND agent_email_clean is not blank:

        create personalized message
        generate message_id
        send email
        update send_status to "Sent"
        update send_date
        save message_id

    ELSE:
        skip record
        keep qa_notes or status reason
```

---

## ✉️ Message Personalization Logic

The public-safe version uses a synthetic message template.

### Example Personalization Fields

* agent_first_name
* campaign_type
* city_cluster
* listing_status
* price_band

### Pseudocode

```text
message_subject = build subject using campaign_type and city_cluster

message_body = template
    replace {{agent_first_name}}
    replace {{city_cluster}}
    replace {{campaign_type}}
    replace {{price_band}}
```

No real email copy, real templates, client names, or company-specific campaign links should be included in this repository.

---

## 👁️ Open Tracking Logic

Open tracking identifies whether a sent message was opened.

### Public-Safe Concept

The original workflow concept can be represented as:

```text
IF tracking event is detected for message_id:
    increase open_count
    IF first_open_date is blank:
        set first_open_date
    update last_open_date
    update send_status to "Opened"
```

### Important Note

This repository must not include:

* Real tracking pixel URLs
* Real web app URLs
* Real Apps Script deployment links
* Real recipient data
* Real message IDs

---

## 🔗 Click Tracking Logic

Click tracking identifies whether a recipient clicked a campaign link.

### Public-Safe Concept

```text
IF click event is detected for message_id:
    increase click_count
    IF first_click_date is blank:
        set first_click_date
    update last_click_date
    update send_status to "Clicked"
```

### Example Public-Safe Click Fields

* click_count
* first_click_date
* last_click_date
* clicked_link_type

Use generic link categories only, such as:

* website
* consultation
* listing_page
* reply_prompt

Do not include real URLs.

---

## 💬 Reply Tracking Logic

Reply tracking identifies whether the recipient responded.

### Public-Safe Concept

```text
Search inbox for replies connected to sent messages.

FOR each sent message:
    IF reply is found:
        update reply_status to "Replied"
        update reply_date
        update send_status to "Replied"
        update final_outcome to "Response Received"
```

### Confidentiality Rule

Do not upload:

* Gmail threads
* Sender or recipient names
* Real email subjects
* Email bodies
* Screenshots from Gmail
* Reply logs

---

## 🔁 Follow-Up Logic

Follow-up logic identifies leads that were contacted but did not respond within a defined window.

### Example Logic

```text
FOR each sent lead:
    IF send_status = "Sent"
    AND days_since_send >= 7
    AND reply_status != "Replied":

        update follow_up_status to "Follow-up Required"
```

### Follow-Up Send Logic

```text
FOR each lead:
    IF follow_up_status = "Follow-up Required"
    AND agent_email_clean is not blank:

        create follow-up message
        send follow-up
        update follow_up_status to "Follow-up Sent"
        update final_outcome to "Follow-up Sent"
```

---

## 🏁 Final Outcome Logic

Each lead should have a final outcome field for reporting.

| Final Outcome      | Meaning                                    |
| ------------------ | ------------------------------------------ |
| Not Sent           | Lead has not been contacted                |
| Sent               | Initial outreach sent                      |
| Opened             | Message was opened                         |
| Clicked            | Recipient clicked a tracked link           |
| Replied            | Recipient replied                          |
| Follow-up Required | No reply after follow-up window            |
| Follow-up Sent     | Follow-up message sent                     |
| Excluded           | Record failed QA or was not campaign-ready |

---

## 📊 Reporting Logic

Automation fields feed campaign analytics.

Example summary metrics:

* total_leads
* sent_count
* opened_count
* clicked_count
* replied_count
* follow_up_required_count
* follow_up_sent_count
* excluded_count

Example rate calculations:

```text
send_rate = sent_count / total_leads

open_rate = opened_count / sent_count

click_rate = clicked_count / sent_count

reply_rate = replied_count / sent_count

follow_up_rate = follow_up_required_count / sent_count
```

If `sent_count = 0`, rates should return `0` or `N/A` to avoid division errors.

---

## 🧪 Automation QA Rules

Automation fields should follow these checks:

| Rule             | Expected Logic                                                 |
| ---------------- | -------------------------------------------------------------- |
| Message ID       | Required when send_status is Sent, Opened, Clicked, or Replied |
| Send date        | Required when send_status is not Not Sent                      |
| Open count       | Must be zero or greater                                        |
| Click count      | Must be zero or greater                                        |
| Reply date       | Required when reply_status is Replied                          |
| Follow-up status | Required for all records                                       |
| Final outcome    | Required for all records                                       |

---

## 🔒 Confidentiality Requirements

This repository uses public-safe automation documentation only.

Do not include:

* Real Apps Script files from the company workflow
* Real deployment URLs
* Real Gmail messages
* Real tracking URLs
* Real message IDs
* Real lead records
* Real agent contact details
* Internal execution logs
* Screenshots from company systems

All automation examples must be synthetic, generalized, and safe for public GitHub use.
