# The Talent Retention Puzzle  
### Uncovering the Hidden Drivers of Employee Attrition  
*A Hypothesis-Driven Exploratory Data Analysis*

---

## Project Overview

This project presents a **portfolio-grade exploratory data analysis (EDA)** that diagnoses the root causes of employee attrition. Moving beyond surface-level correlations, the analysis adopts a **hypothesis-driven framework** to systematically evaluate competing explanations and translate insights into **actionable retention strategies**.

---

## The Business Problem

Over the past 12 months, the Engineering and Sales departments have experienced **elevated resignation rates**. Exit interviews cite vague explanations—*“better opportunities”* and *“burnout”*—leaving leadership without clear direction on how to respond.

**Central Question:**  
> *Is employee attrition primarily driven by compensation, or are deeper cultural, managerial, and environmental factors at play?*

---

## Key Findings

### Hypothesis Testing Results

| Hypothesis | Evidence | Verdict |
|---------|--------|--------|
| **H1: Compensation** | Income gaps exist but are moderate; stock options show a strong protective effect | ⚠️ Partial Support |
| **H2: Burnout** | Overtime is the strongest predictor; work-life balance is critical; effects are multiplicative | ✅ Strong Support |
| **H3: Environment** | Relationship satisfaction and manager tenure matter; secondary to workload | 📊 Moderate Support |

---

### Critical Insights

- **Burnout is the #1 Driver**  
  Employees working overtime are **2× more likely to leave** than those without overtime.

- **Stock Options Are Highly Protective**  
  The transition from **0 → 1 stock option** yields the single largest reduction in attrition risk.

- **First-Year Employees Are Most Vulnerable**  
  Attrition among employees with <1 year tenure is **~25% higher than average**.

- **Interactions Matter**  
  Employees with **overtime + no stock options** experience **35%+ attrition rates**.

- **Sales Department Requires Immediate Attention**  
  Highest attrition overall and heightened sensitivity to promotion stagnation.

---

### Counterintuitive Findings

- **Commute Distance Affects Junior Employees More Than Seniors**  
  Senior employees appear “anchored” by institutional knowledge and internal networks.

- **Promotion Stagnation Impacts Sales More Than R&D**  
  Sales roles are more externally benchmarked and opportunity-sensitive.

- **Stock Options Exhibit Diminishing Returns**  
  The **initial grant** provides the largest marginal retention benefit.

---

## 📊 The Analysis

### Dataset
- **Source:** IBM HR Analytics Employee Attrition Dataset  
- **Size:** 1,470 employees × 35 features  
- **Target Variable:** Attrition (Yes / No)

### Methodology
- **Problem Framing:** Defined attrition risk and prioritized high-value employee segments  
- **Data Preparation:** Quality assessment, feature engineering, cohort creation  
- **Hypothesis Testing:** Systematic evaluation of compensation, burnout, and environment drivers  
- **Feature Interaction Analysis:** Identification of compound risk factors  
- **Risk Profiling:** Composite risk scoring for targeted intervention  
- **Synthesis:** Translation of insights into retention strategy recommendations  

---

## Strategic Recommendations

### Recommendation 1: Overtime Management Program
- Implement mandatory overtime caps (≤40 hours/month)  
- Add headcount in chronic high-overtime teams  
- Offer comp time for unavoidable overtime  

**Estimated Impact:** ~15–20 fewer departures annually  

---

### Recommendation 2: Universal Stock Option Program
- Extend stock option eligibility to all full-time employees  
- Prioritize **0 → 1** option grants (highest marginal impact)  
- Consider RSUs for non-exempt roles  

**Estimated Impact:** ~10–15 fewer departures annually  

---

### Recommendation 3: New Hire Retention Program
- Structured 90-day onboarding program  
- Mandatory mentor assignment for all new hires  
- 30 / 60 / 90-day check-ins with skip-level managers  
- Hybrid or remote flexibility for long-commute employees  

**Estimated Impact:** ~5–10 fewer departures annually  

---

### Total Expected Impact

- **Projected Attrition Reduction:** 25–35%  
- **Estimated Annual Savings:** $500K–$1M+ in replacement and productivity costs  

---

## Repository Structure

```
hr_analytics_project/
├── Talent_Retention_Puzzle_Analysis.ipynb    # Complete Jupyter notebook
├── hr_employee_attrition.csv                 # Dataset
├── README.md                                 # This file
├── RETENTION_STRATEGY_MEMO.md                # Executive summary memo
└── outputs/
    ├── 01_overview.png                       # Cohort and department overview
    ├── 02_key_factors.png                    # Compensation and burnout factors
    ├── 03_interactions.png                   # Feature interactions
    ├── 04_feature_importance.png             # Correlation analysis
    ├── 05_risk_profile.png                   # Risk score analysis
    └── high_risk_employees.csv               # High-risk employee list
```

---

## How to Run This Project

This project is designed to be run as a Jupyter Notebook.

1. Create and activate a Python virtual environment  
2. Install dependencies from `requirements.txt`  
3. Add the dataset to `data/raw/`  
4. Run all cells in `Talent_Retention_Puzzle_Analysis.ipynb`

---

## Technical Stack

- **Python 3.x**
- **pandas** — data manipulation  
- **numpy** — numerical computing  
- **matplotlib / seaborn** — visualization  
- **scipy** — statistical testing  

---

## Value of the Insights

This analysis delivers:

- **Prioritized understanding** of attrition drivers (burnout > compensation > environment)  
- **Targeted interventions** with quantifiable business impact  
- **Risk identification** via composite scoring  
- **Cost justification** for retention investments  
- **Counterintuitive insights** that challenge conventional assumptions  

---

## Next Steps

- Build a **predictive attrition model** (ML-based risk scoring)  
- Conduct **stay interviews** with high-risk employees  
- Implement **A/B testing** of retention interventions  
- Develop a **real-time attrition monitoring dashboard**

---

## Author

**Soham Chavan**  
Undergraduate Student — Data Science  
Pennsylvania State University

---

## License

This project uses the publicly available IBM HR Analytics dataset. All analysis and code are provided for educational and demonstration purposes.
