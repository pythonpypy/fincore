{{ config(materialized='table') }}

SELECT
    account_id,
    account_code,
    account_name,
    account_type,
    normal_balance,
    CASE
        WHEN normal_balance = 'Debit' THEN true
        ELSE false
    END AS is_debit_normal
FROM {{ ref('stg_accounts') }}
