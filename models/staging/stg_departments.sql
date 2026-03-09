{{ config(materialized='view') }}

SELECT
    department_id,
    department_code,
    department_name
FROM {{ ref('departments') }}
