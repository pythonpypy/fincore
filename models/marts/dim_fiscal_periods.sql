{{ config(materialized='table') }}

SELECT
    period_id,
    period_name,
    period_label,
    month,
    quarter,
    year,
    start_date,
    end_date,
    CASE
        WHEN year = 2025 THEN true
        ELSE false
    END AS is_current_year
FROM {{ ref('stg_fiscal_periods') }}
