---
title: Department Spending
---
# Department Spending
```sql dept_totals
SELECT department_name, SUM(total_expenses) AS total_spent
FROM monthly_expenses
GROUP BY department_name
ORDER BY total_spent DESC
```
```sql dept_monthly
SELECT department_name, total_expenses,
    year::varchar || '-' || lpad(month::varchar, 2, '0') || '-01' AS period_date
FROM monthly_expenses ORDER BY year, month
```

<BarChart data={dept_totals} x=department_name y=total_spent title='Total Spend by Department 2023-2025'/>

<LineChart data={dept_monthly} x=period_date y=total_expenses series=department_name title='Monthly Spend by Department' sort=false/>
