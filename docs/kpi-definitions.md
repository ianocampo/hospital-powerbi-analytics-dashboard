# KPI Definitions and Baseline Values

The values below are transcribed from **Section VI, page 14 of the approved 15-page Executive Case Study** (October 2026). They are the report's metric definitions and results, **not extracted DAX source expressions**. Do not present them as literal DAX code without inspecting the native model.

| KPI | Conceptual definition | Overall reported result |
| :--- | :--- | ---: |
| Total Encounters | Count encounter rows | **27,891** |
| Unique Patients | Distinct encounter patient identifiers | **974** |
| Total Procedures | Count linked procedure records | **47,701** |
| Total Claim Cost | Sum of recorded claim cost | **$101,514,375.52** |
| Total Payer Coverage | Sum of recorded payer coverage | **$31,097,506.99** |
| Average Claim Cost | Total Claim Cost / Total Encounters | **$3,639.68** |
| Zero Coverage Encounters | Sum of zero-coverage flags | **13,586** |
| Zero Coverage % | Zero Coverage Encounters / Total Encounters | **48.71%** |
| Coverage % | Total Payer Coverage / Total Claim Cost | **30.63%** |
| Encounters per Patient | Total Encounters / Unique Patients | **28.64** |
| Procedures per Encounter | Total Procedures / Total Encounters | **1.71** |
| Average Duration Hours | Average valid encounter duration | **1.84 hours** |
| Inpatient Encounters | Sum of inpatient flags | **1,135** |
| Emergency Encounters | Sum of emergency flags | **2,322** |

## Interpretation
- Overall figures include **Jan–6 Feb 2022**, while annual visuals end in **2021**.
- The report uses zero **recorded** payer coverage, not proven unpaid balances.
- **89** zero-coverage rows have zero claim costs; **13,497** positive-claim-cost rows have zero recorded payer coverage.
- **Coverage %** is cost-weighted rather than a percentage of visits with coverage.
- **28.64 encounters per patient** is a full-observation-window ratio, not an annual visit frequency.
- Average duration hours is based on records meeting the report's valid-duration rule; it is not automatically a bed occupancy or inpatient length-of-stay measure.
- Functions identified in the report include COUNTROWS, DISTINCTCOUNT, SUM, DIVIDE and AVERAGE. Exact formulas and model dependencies require inspection of the final approved native Power BI model.
