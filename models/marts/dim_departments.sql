{{ config(materialized='table') }}

SELECT
    department_id,
    department_code,
    department_name
FROM {{ ref('stg_departments') }}
