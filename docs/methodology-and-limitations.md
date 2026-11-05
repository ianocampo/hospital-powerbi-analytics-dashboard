# Methodology, Evidence and Limitations

## Source and scope
Synthetic Maven Analytics Hospital Patient Records, with patient, payer, organization, encounter and procedure records. The model includes date-related analytical attributes. Period: 2 January 2011 to 6 February 2022; annual charts stop at the last complete year, 2021.

## Report views and decision questions
1. **Executive Overview:** overall reach, visits, procedures, recorded costs, coverage and change across years.
2. **Encounters & Utilization:** activity and procedure concentration, visit duration and service intensity.
3. **Financial & Coverage:** payer-level cost and zero-coverage patterns, including insured versus no-insurance contexts.
4. **Patient Behavior:** demographics, cohorts, repeat utilization and service demand.

## Model architecture as described in the case study
The report combines encounters and procedures with patient, payer, organization and date dimensions. The approved report mentions single-direction relationships and Power Query work. Its six recurring filters are **Year**, **Encounter class**, **Payer**, **Age group**, **Gender** and **Month**.

An earlier technical change log compares an original PBIX with a separately generated semantic-model variant. These were **not necessarily identical saved reports**. We therefore do not infer exact current relationship counts or export unverified DAX scripts from those earlier variants.

## Analytical boundaries
- The `No_Insurance` category is a **recorded group**, not proof of collectability.
- Zero payer coverage does not prove an outstanding debt. Reconcile billing, eligibility and actual payment records.
- Long-duration and short-duration service interpretations depend on the report's validation rules.
- Patient repeat use is not necessarily avoidable utilization or readmission.
- Clinical and operational recommendations need context from service leaders, not just administrative patterns.
- The source dataset is synthetic; metrics are demonstrations, **not** contemporary hospital performance indicators.

## Reproducibility status (at packaging)
- **Verified:** 15-page client-facing case study; four authentic 1920×1080 screenshots; summary metrics and described model documentation.
- **Not yet verified:** original approved `.pbix` or `.pbip` files; current DAX source expressions; successful fresh-machine Power BI Desktop open, data refresh, report interactions, or PBIP export.

## What is needed for a source-enabled release
Retrieve the actual **final** Power BI Desktop file, compare the four pages and metrics with approved visuals, validate all filters and relationships, change data-source paths to safe/reproducible locations, then export a tested PBIP/TMDL project. Preserve the original report as read-only during conversion.
