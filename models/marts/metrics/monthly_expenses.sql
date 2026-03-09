{{ config(materialized='table') }}

SELECT
    fp.year,
    fp.month,
    fp.period_name,
    fp.period_label,
    fp.quarter,
    d.department_name,
    SUM(f.debit_amount) AS total_expenses
FROM {{ ref('fact_journal_lines') }} f
JOIN {{ ref('dim_accounts') }} a
    ON f.account_id = a.account_id
JOIN {{ ref('dim_fiscal_periods') }} fp
    ON f.period_id = fp.period_id
JOIN {{ ref('dim_departments') }} d
    ON f.department_id = d.department_id
WHERE a.account_type = 'Expense'
GROUP BY
    fp.year,
    fp.month,
    fp.period_name,
    fp.period_label,
    fp.quarter,
    d.department_name
ORDER BY
    fp.year,
    fp.month
