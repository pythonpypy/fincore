{{ config(materialized='table') }}

WITH revenue AS (
    SELECT
        period_id,
        SUM(credit_amount) AS total_revenue
    FROM {{ ref('fact_journal_lines') }} f
    JOIN {{ ref('dim_accounts') }} a
        ON f.account_id = a.account_id
    WHERE a.account_type = 'Revenue'
    GROUP BY period_id
),
expenses AS (
    SELECT
        period_id,
        SUM(debit_amount) AS total_expenses
    FROM {{ ref('fact_journal_lines') }} f
    JOIN {{ ref('dim_accounts') }} a
        ON f.account_id = a.account_id
    WHERE a.account_type = 'Expense'
    GROUP BY period_id
)
SELECT
    fp.year,
    fp.month,
    fp.period_name,
    fp.period_label,
    fp.quarter,
    r.total_revenue,
    e.total_expenses,
    r.total_revenue - e.total_expenses AS net_profit
FROM {{ ref('dim_fiscal_periods') }} fp
LEFT JOIN revenue r ON fp.period_id = r.period_id
LEFT JOIN expenses e ON fp.period_id = e.period_id
ORDER BY fp.year, fp.month
