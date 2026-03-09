{{ config(materialized='table') }}

SELECT
    l.line_id,
    l.entry_id,
    l.account_id,
    l.department_id,
    e.period_id,
    e.entry_date,
    l.debit_amount,
    l.credit_amount,
    l.net_amount,
    l.description
FROM {{ ref('stg_journal_entry_lines') }} l
LEFT JOIN {{ ref('stg_journal_entries') }} e
    ON l.entry_id = e.entry_id
