
    
    



select count(*) as validation_errors
from `dbt-demos`.`dbt_blake`.`stg_customers`
where customer_id is null


