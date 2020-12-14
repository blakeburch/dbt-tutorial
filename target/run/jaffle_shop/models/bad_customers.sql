

  create or replace table `dbt-demos`.`dbt_blake`.`bad_customers`
  
  
  OPTIONS()
  as (
    select * from `dbt-demos`.`dbt_blake`.`customers` where number_of_orders = 0
  );
    