# 🏙️ NYC Building Complaint-to-Violation Analysis

> Measuring how often 311 Department of Buildings complaints lead to formal violations — and holding NYC accountable for its enforcement.

---

## 📋 Table of Contents

- [Problem Statement](#-problem-statement)
- [Datasets](#-datasets)
- [Real-World Applicability](#-real-world-applicability)
- [Limitations](#-limitations)
- [Roadmap & Scaling](#-roadmap--scaling)

---

## 🔍 Problem Statement

Every year, thousands of NYC residents submit complaints about unsafe building conditions, code violations, and illegal construction through 311. But how often does a complaint actually lead to a formal violation?

This project addresses **public sector accountability** within NYC's housing and building enforcement systems. By connecting 311 complaint data to DOB violation records, we aim to answer:

- How responsive is NYC enforcement to resident reports?
- Does a higher volume of complaints about the same building increase the likelihood of a formal violation being issued?
- Are there patterns across boroughs in how complaints are handled?

---

## 📊 Datasets

| Source | Dataset | Link |
|--------|---------|------|
| NYC Open Data | DOB Complaints Received | [View Dataset](https://data.cityofnewyork.us/Housing-Development/DOB-Complaints-Received/eabe-havv/about_data) |
| NYC Open Data | DOB Violations | [View Dataset](https://data.cityofnewyork.us/Housing-Development/DOB-Violations/3h2n-5cm9/about_data) |
| Kaggle | NYC 311 Requests | [View Dataset](https://www.kaggle.com/datasets/pearsejim01/nyc-311-requests) |

---

## 🌍 Real-World Applicability

This tool gives residents, researchers, and policymakers a data-driven view of how effectively NYC responds to building-related complaints.

By identifying buildings with repeated complaints that **never escalate to violations**, the program can:

- Surface potential gaps in enforcement
- Highlight where city resources may need to be redirected
- Provide transparency into the DOB's complaint resolution process

---

## ⚠️ Limitations

**Borough mapping gap**
The DOB Violations dataset includes only street addresses — no borough field. A geocoding or address-matching solution is required to map violations to specific boroughs for geographic analysis.

**Single complaint source**
Currently, the only complaint input is 311 calls. This excludes complaints filed through other channels, which may underrepresent certain issues or neighborhoods.

**Duplicate caller problem**
The 311 system does not distinguish between multiple calls made by the same person about the same issue, which can inflate complaint volume counts and skew analysis.

---

## 🚀 Roadmap & Scaling

### Live Data Integration
Replace static datasets with live feeds from NYC Open Data's DOB Complaints and DOB Violations endpoints to refresh the analysis daily or weekly.

### Ticket System
Introduce a tracking system that assigns unique tickets to each complaint, enabling:
- Accurate tracking of individual cases over time
- Deduplication of repeat calls from the same caller about the same issue
- Follow-up capability that the current 311 system lacks

### Borough-Level Analysis
Implement geocoding to resolve the address-only limitation in the DOB Violations dataset, enabling full borough-level breakdowns and mapping.
