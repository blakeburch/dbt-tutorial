

  create or replace view `dbt-demos`.`dbt_blake`.`my_second_dbt_model`
  OPTIONS()
  as -- Use the `ref` function to select from other models

select *
from `dbt-demos`.`dbt_blake`.`my_first_dbt_model`
where id = 1;

