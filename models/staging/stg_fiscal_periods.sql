{{ config(materialized='view') }}

SELECT
    period_id,
    period_name,
    month,
    quarter,
    year,
    start_date,
    end_date,
    'Q' || quarter || ' ' || year AS period_label
FROM {{ ref('fiscal_periods') }}
