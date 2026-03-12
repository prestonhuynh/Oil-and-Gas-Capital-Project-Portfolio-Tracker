### Oil and Gas Capital Project Portfolio Tracker
An Excel-based portfolio tracker analyzing capital project performance for a fictional O&G operator, Meridian Energy Group. Built to surface cost overruns, schedule slippage, change order impact, and overall portfolio health across 50 synthetic projects.

## Tools
 • Python (data generation: pandas, numpy, faker)\
 • Microsoft Excel (Power Query, XLOOKUP, INDEX/MATCH, SUMIFS/COUNTIFS, IFS, IFERROR, Pivot Tables, Conditional Formatting, Data Validation)

## Dataset
Generated synthetically using Python with a fixed random seed for reproducibility. 50 projects across 4 project types and 4 Oil & Gas regions.

# Raw Fields:
 • ``Project_ID``, ``Project_Name``, ``Project_Type``, ``Region, Operator``, ``Subcontractor``, ``Status``\
 • ``Budgeted_Cost``, ``Actual_Cost``\
 • Phase costs: ``Phase_Planning``, ``Phase_Drilling_Construction``, ``Phase_Completion``, ``Phase_Closeout``\
 • ``Planned_Start``, ``Planned_End``, ``Actual_End``, ``Schedule_Variance_Days``\
 • ``Change_Order_Count``, ``Change_Order_Cost``

# Calculated Fields:
 • ``Cost_Variance`` — Actual minus budgeted cost\
 • ``Cost_Variance_Pct`` — Variance as % of budget\
 • ``Change_Order_Budget_Impact_Pct`` — Change order cost as % of budget\
 • ``On_Time`` — Yes/No based on schedule variance

# Derived Flags (Excel):
 • ``Risk_Flag`` — High/Medium/Clean based on cost variance and on-time status\
 • ``Budget_Health`` — Critical/Watch/On Track/Under Budget based on variance %\
 • ``Change_Order_Risk`` — High/Moderate/Low/No Change Orders based on CO impact %

## Excel Skills Demonstrated
 • Power Query — CSV import pipeline with typed columns and named query\
 • XLOOKUP — Dynamic top 5 over-budget project lookup\
 • SUMIFS/COUNTIFS — Region-filtered KPI cards\
 • IFS/Nested logic — Risk_Flag, Budget_Health, Change_Order_Risk classification\
 • IFERROR — Error handling across all derived columns\
 • Pivot Tables — Average cost variance by project type, average schedule variance by region\
 • Data Validation — Region filter dropdown, Status column restriction\
 • Conditional Formatting — Color scale on Top 5 variance column

## Dashboard
 • Portfolio health KPI cards: Total Budget, Total Actual Cost, Cost Variance, On-Time Rate\
 • Dynamic region filter with live KPI cards updating by region\
 • Top 5 over-budget projects table with conditional formatting\
 • Average cost variance % by project type (bar chart)\
 • Average schedule variance by region in days (bar chart)

## Key Findings
 • Portfolio total budget: $375,070,028 vs actual cost: $379,205,869 — $4,135,841 over budget overall\
 • On-time delivery rate: 50% across all 50 projects\
 • 12 projects flagged High Risk, 26 Medium Risk, 12 Clean\
 • 13 projects Critical on budget health, 15 Under Budget\
 • Top over-budget project: OG-1009 — Midland Pipeline Construction at 22.0% over budget

## Files
 • ``generate_data.py`` — Synthetic dataset generator\
 • ``oil_and_gas_project_data.csv`` — Generated source data\
 • ``Oil_and_Gas_Capital_Project_Portfolio.xlsx`` — Full workbook with Data, Dashboard, and Pivots sheets
