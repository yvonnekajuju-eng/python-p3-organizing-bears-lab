# lib/sql_queries.py

# 1. Select all female bears: name and age
select_all_female_bears_return_name_and_age = """
SELECT name, age
FROM bears
WHERE sex='F';
"""

# 2. Select all bears' names and orders alphabetically
select_all_bears_names_and_orders_in_alphabetical_order = """
SELECT name
FROM bears
ORDER BY name ASC;
"""

# 3. Select all bears' names and ages that are alive, order youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELECT name, age
FROM bears
WHERE alive=1
ORDER BY age ASC;
"""

# 4. Select the oldest bear and return name and age
select_oldest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age DESC
LIMIT 1;
"""

# 5. Select the youngest bear and return name and age
select_youngest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age ASC
LIMIT 1;
"""

# 6. Count bears grouped by color
select_bear_count_grouped_by_color = """
SELECT color, COUNT(*)
FROM bears
GROUP BY color;
"""

# 7. Select bears with temperament 'aggressive'
select_bears_with_aggressive_temperament = """
SELECT *
FROM bears
WHERE temperament='aggressive';
"""

# 8. Select bears that are alive and male
select_alive_male_bears = """
SELECT *
FROM bears
WHERE alive=1 AND sex='M';
"""
