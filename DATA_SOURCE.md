# Data Source and Native Power BI Project

**Native source:** [Download original PBIX](powerbi/IanOcampo_PBI_Capstone.pbix).

Synthetic **Maven Analytics Hospital Patient Records**, sourced from SyntheticMass. Four-page Power BI Desktop report; not a real hospital commission. Original PBIX structurally contains a binary Data Model, four-page report definition, visual resource files and filter/navigation elements. The owner opened it in Power BI Desktop, but independent complete-refresh and DAX-result reconciliation remain outside this structural verification.

**Native-file SHA-256:** `1da76016654dc03470848013010c77241b20bcfb072d3bd2c6d2fac7a078b6d8`.


## Download the original hospital dataset

**Official dataset:** [Hospital Patient Records — Maven Analytics Data Playground](https://mavenanalytics.io/data-playground/hospital-patient-records)

Maven identifies the source as **SyntheticMass**, describes the records as synthetic hospital-patient data, and lists the dataset license as **Public Domain**. The original multi-table CSV dataset can be obtained from Maven's page; sign-in or sign-up may be required for the download.

The downloadable [Power BI report (.pbix)](powerbi/IanOcampo_PBI_Capstone.pbix) already contains a saved embedded Data Model, so readers can inspect the actual report without a separate CSV download. To independently reconstruct or refresh the import, download the source tables, review **Home → Transform data → Data source settings** inside Power BI Desktop, update any local data-source paths, then refresh and reconcile the KPIs against [the KPI dictionary](docs/kpi-definitions.md). A successful fresh-computer refresh has **not** been independently verified.

The dataset link is maintained by Maven Analytics, not this repository. This repository does not present synthetic records as real patient information.
