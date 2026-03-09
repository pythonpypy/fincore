{{ config(materialized='view') }}

SELECT
    line_id,
    entry_id,
    account_id,
    department_id,
    debit_amount,
    credit_amount,
    debit_amount - credit_amount AS net_amount,
    description
FROM {{ ref('journal_entry_lines') }}
