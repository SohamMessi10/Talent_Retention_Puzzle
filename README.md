# The Talent Retention Puzzle (EDA + Hypothesis Testing)

An exploratory data analysis project that investigates *why* attrition spiked in **Engineering** and **Sales** over the last 12 months, using hypothesis testing via visualization and feature-interaction analysis.

## Business question
> Is employee attrition primarily driven by compensation, or are deeper behavioral, managerial, and environmental factors at play?

## Business Objectives
- Identify high-risk employee segments based on tenure, age, workload, and satisfication metrics
- Test competing hypotheses around compensation, burnout, and workplace environment
- Quantify attrition risk patterns across employee cohorts
- Translate finding into practical, low-cost retention interventions

## Dataset
**Source**: IBM HR Analytics Employee Attrition & Performance Dataset (Kaggle).

**Size**: ~1,470 employees x 35 features

### Key Features 
- Demographics(Age, Distance from Home)
- Job attributes (Department, Job Role, Overtime)
- Satification metrics (Job, Relationship, Work-Life Balance)
- Career progression (Years at Company, Promotion)
- Attrition indication (yes/no)


## Project structure
```
.
├── notebooks/                       # analysis notebook(s)
├── src/                             # helper code (optional)
├── data/
│   ├── raw/                         # raw dataset (ignored by git)
│   └── processed/                   # processed data (ignored by git)
├── outputs/                         # generated artifacts (ignored by git)
├── reports/
│   ├── Retention_Strategy_Memo.docx # stakeholder memo
│   └── figures/                     # figures used in README
├── requirements.txt
└── README.md
```

## Key deliverables
- Reproducible Jupyter Notebook with full EDA and hypothesis testing
- Saved visualizations for reporting and presentation
- Executive-facing Retention Strategy Memo with actionable insights
- Data-driven recomnedation for reducing employe attrition.


## 🔍 Analytical Approach

This project follows a **structured EDA workflow** designed to mirror real-world analytics work.

### 1. Data Preparation
- Cleaned categorical inconsistencies  
- Engineered:
  - **Tenure Cohorts** (Onboarding → Veteran)  
  - **Age Cohorts**  
  - **Binary Attrition Flag**

### 2. Hypothesis-Driven Exploration
Key hypotheses tested include:
- **Compensation Hypothesis**: Are lower-paid employees more likely to leave?  
- **Burnout Hypothesis**: Does overtime combined with low satisfaction accelerate attrition?  
- **Environment Hypothesis**: Do managerial relationships differ across departments?  
- **Mobility Hypothesis**: Does commute distance disproportionately impact junior employees?

### 3. Cohort & Interaction Analysis
- Attrition rates analyzed across **intersecting variables**  
- Focus on identifying **combinations of risk factors**, not single drivers

### 4. Business Synthesis
Insights translated into:
- Clear visualizations  
- Quantified risk statements  
- Actionable HR recommendations


## How to run
This project is designed to be run as a Jupyter Notebook.

1. Create and activate a Python virtual environment  
2. Install dependencies from `requirements.txt`  
3. Add the dataset to `data/raw/`  
4. Run all cells in `notebooks/Talent_Retention_Puzzle_Analysis.ipynb`

```
## Results preview
![Cohort overview](reports/figures/01_overview.png)
![Key factors](reports/figures/02_key_factors.png)

## Notes
- The notebook creates `outputs/` automatically (for saved charts and CSV exports).
- If you want to version outputs/figures, adjust `.gitignore` accordingly.
