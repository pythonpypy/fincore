{{ config(materialized='table') }}

SELECT
    fp.year,
    fp.month,
    fp.period_name,
    fp.period_label,
    fp.quarter,
    SUM(f.credit_amount) AS total_revenue
FROM {{ ref('fact_journal_lines') }} f
JOIN {{ ref('dim_accounts') }} a
    ON f.account_id = a.account_id
JOIN {{ ref('dim_fiscal_periods') }} fp
    ON f.period_id = fp.period_id
WHERE a.account_type = 'Revenue'
GROUP BY
    fp.year,
    fp.month,
    fp.period_name,
    fp.period_label,
    fp.quarter
ORDER BY
    fp.year,
    fp.month
