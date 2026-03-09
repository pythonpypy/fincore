---
title: FinCore Financial Dashboard
---
# FinCore Financial Dashboard
A 3-year financial analysis of company performance from 2023 to 2025.

## Key Metrics
```sql kpi
SELECT
    SUM(total_revenue) AS total_revenue,
    SUM(total_expenses) AS total_expenses,
    SUM(net_profit) AS net_profit
FROM net_profit
```
<BigValue data={kpi} value=total_revenue title='Total Revenue' fmt=usd/>
<BigValue data={kpi} value=total_expenses title='Total Expenses' fmt=usd/>
<BigValue data={kpi} value=net_profit title='Net Profit' fmt=usd/>

## Monthly Revenue
```sql revenue
SELECT year, month, total_revenue,
    year::varchar || '-' || lpad(month::varchar, 2, '0') || '-01' AS period_date
FROM net_profit ORDER BY year, month
```
<LineChart data={revenue} x=period_date y=total_revenue title='Monthly Revenue 2023-2025' sort=false/>

## Net Profit by Month
```sql profit
SELECT year, month, total_revenue, total_expenses, net_profit,
    year::varchar || '-' || lpad(month::varchar, 2, '0') || '-01' AS period_date
FROM net_profit ORDER BY year, month
```
<BarChart data={profit} x=period_date y=net_profit title='Net Profit by Month' sort=false/>
