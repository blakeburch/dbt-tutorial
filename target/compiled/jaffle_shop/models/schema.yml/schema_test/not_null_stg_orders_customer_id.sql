
    
    



select count(*) as validation_errors
from `dbt-demos`.`dbt_blake`.`stg_orders`
where customer_id is null


