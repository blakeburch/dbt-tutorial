
    
    



select count(*) as validation_errors
from `dbt-demos`.`dbt_blake`.`customers`
where customer_id is null


