# The Talent Retention Puzzle
## Uncovering the Hidden Drivers of Employee Attrition

### A Hypothesis-Driven Exploratory Data Analysis

---

## 📋 Project Overview

This project presents a comprehensive, portfolio-grade exploratory data analysis (EDA) that diagnoses the root causes of employee attrition. Moving beyond surface-level analysis, this project adopts a **hypothesis-driven approach** to systematically test competing explanations and deliver actionable recommendations.

### The Business Problem

Over the past 12 months, our Engineering and Sales departments have experienced elevated resignation rates. Exit interviews provide vague explanations—"better opportunities" and "burnout"—leaving leadership uncertain about how to respond.

**Central Question:** *Is employee attrition primarily driven by compensation, or are deeper cultural, managerial, and environmental factors at play?*

---

## 🎯 Key Findings

### Hypothesis Testing Results

| Hypothesis | Evidence | Verdict |
|------------|----------|---------|
| **H1: Compensation** | Income gap exists but moderate; stock options show strong protective effect | ⚠️ Partial Support |
| **H2: Burnout** | Overtime is top predictor; work-life balance critical; combined effects multiplicative | ✅ Strong Support |
| **H3: Environment** | Environment satisfaction matters; manager tenure helps; secondary to workload | 📊 Moderate Support |

### Critical Insights

1. **Burnout is the #1 Driver**: Employees working overtime are **2x+ more likely** to leave
2. **Stock Options are Protective**: Moving from 0 to 1 stock options has the biggest retention impact
3. **First-Year Employees are Vulnerable**: ~25% higher attrition than average
4. **Interactions Matter**: Overtime + No Stock Options = **35%+ attrition rate**
5. **Sales Department Needs Attention**: Highest attrition + promotion sensitivity

### Counterintuitive Findings

- **Distance from home affects juniors more than seniors** - Senior employees are "anchored" by relationships and institutional knowledge
- **Promotion stagnation hits Sales harder than R&D** - Sales roles are more externally benchmarked
- **Stock options have diminishing returns** - The 0→1 transition provides the biggest impact

---

## 📊 The Analysis

### Dataset
- **Source**: IBM HR Analytics Employee Attrition Dataset
- **Size**: 1,470 employees × 35 features
- **Target**: Attrition (Yes/No)

### Methodology

1. **Problem Framing**: Defined attrition risk and identified high-value employee segments
2. **Data Preparation**: Quality assessment, feature engineering, cohort creation
3. **Hypothesis Testing**: Systematically tested compensation, burnout, and environment hypotheses
4. **Feature Interactions**: Identified compound risk factors
5. **Risk Profiling**: Created composite risk scores for targeted intervention
6. **Recommendations**: Developed data-backed retention strategies

---

## 💡 Strategic Recommendations

### Recommendation 1: Overtime Management Program
- Implement mandatory overtime caps (40 hrs OT/month max)
- Hire additional headcount in high-OT departments
- Provide comp time for unavoidable overtime
- **Estimated Impact**: ~15-20 fewer departures annually

### Recommendation 2: Universal Stock Option Program
- Extend stock option eligibility to all FTEs
- Focus on Level 0 → 1 transition (biggest impact)
- Consider RSUs for non-exempt employees
- **Estimated Impact**: ~10-15 fewer departures annually

### Recommendation 3: New Hire Retention Program
- 90-day structured onboarding program
- Mandatory mentor assignment for all new hires
- 30/60/90 day check-ins with skip-level manager
- Remote/hybrid flexibility for long-commute employees
- **Estimated Impact**: ~5-10 fewer departures annually

### Total Expected Impact
- **Projected attrition reduction**: 25-35%
- **Estimated annual savings**: $500K-$1M+ in replacement costs

---

## 📁 Repository Structure

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

## 🛠️ Technical Stack

- **Python 3.x**
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **matplotlib** & **seaborn** - Visualization
- **scipy** - Statistical testing

---

## 📈 Value of the Insights

This analysis provides:

1. **Prioritized Understanding**: Clear hierarchy of attrition drivers (burnout > compensation > environment)
2. **Targeted Interventions**: Specific, actionable recommendations with estimated ROI
3. **Risk Identification**: Composite scoring system to identify at-risk employees
4. **Cost Quantification**: Business case for retention investments
5. **Counterintuitive Insights**: Hidden patterns that challenge conventional assumptions

---

## 🔗 Next Steps

1. **Predictive Modeling**: Build ML model to predict individual attrition probability
2. **Stay Interviews**: Conduct targeted interviews with high-risk employees
3. **Intervention Tracking**: Implement A/B testing of retention strategies
4. **Continuous Monitoring**: Build dashboard for real-time attrition tracking

---

## 👤 Author

Data Science Team | HR Analytics Initiative

*This analysis was conducted as part of a strategic workforce planning initiative to improve employee retention and reduce turnover costs.*

---

## 📄 License

This project uses the publicly available IBM HR Analytics dataset. Analysis and code are provided for educational and demonstration purposes.
