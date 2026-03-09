{{ config(materialized='view') }}

SELECT
    account_id,
    account_code,
    account_name,
    account_type,
    normal_balance
FROM {{ ref('accounts') }}
