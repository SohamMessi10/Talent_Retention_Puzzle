# Data

This project uses the **IBM HR Analytics Employee Attrition & Performance** dataset (popularly hosted on Kaggle).

## Option A — Use the included local copy
For convenience, this repo zip includes:

- `data/raw/hr_employee_attrition.csv`

**Do not commit the raw dataset to GitHub** unless you’re sure you’re allowed to.  
The `.gitignore` is set to ignore `data/raw/*` by default.

## Option B — Download fresh
1. Download the dataset from Kaggle.
2. Place the CSV at:

`data/raw/hr_employee_attrition.csv`

## Expected columns
The analysis expects columns like `Attrition`, `Department`, `MonthlyIncome`, `OverTime`, `YearsAtCompany`, `Age`, etc.
