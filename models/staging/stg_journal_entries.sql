{{ config(materialized='view') }}

SELECT
    entry_id,
    CAST(entry_date AS DATE) AS entry_date,
    description,
    reference,
    period_id
FROM {{ ref('journal_entries') }}
