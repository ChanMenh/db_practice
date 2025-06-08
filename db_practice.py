import sqlite3
import pandas as pd

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('STAFF.db')

# Define table name and column names
table_name = 'Departments'
attribute_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'lOC_ID']

# Load CSV file into a DataFrame, assigning custom column names
file_path = '/home/project/Departments.csv'
df = pd.read_csv(file_path, names=attribute_list)

# Create the table and insert the DataFrame into the SQLite database
# 'replace' will drop and recreate the table if it already exists
df.to_sql(table_name, conn, if_exists='replace', index=False)
print('Table is ready')

# Query 1: Select all records from the table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Query 2: Select only the department names
query_statement = f"SELECT DEP_NAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Query 3: Count the total number of records in the table
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Prepare new data to append as a row in the Departments table
data_dict = {
    'DEPT_ID': [9],
    'DEP_NAME': ['Quality Assurance'],
    'MANAGER_ID': [30010],
    'LOC_ID': ['L0010']
}
data_append = pd.DataFrame(data_dict)

# Append the new row to the existing table without replacing it
data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('Data appended successfully')

# Close the database connection
conn.close()
