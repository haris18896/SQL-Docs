import psycopg2

# Paths to the CSV files
csv_files = {
"company_dim": "/Users/harisahmad/Downloads/0-data/1-Confidential/1-personal/SQL-Docs/csv_files/company_dim.csv",
    "skills_dim": "/Users/harisahmad/Downloads/0-data/1-Confidential/1-personal/SQL-Docs/csv_files/skills_dim.csv",
    "job_postings_fact": "/Users/harisahmad/Downloads/0-data/1-Confidential/1-personal/SQL-Docs/csv_files/job_postings_fact.csv",
    "skills_job_dim": "/Users/harisahmad/Downloads/0-data/1-Confidential/1-personal/SQL-Docs/csv_files/skills_job_dim.csv"
}

# Database connection parameters
db_params = {
    "dbname": "sql_course",
    "user": "postgres",
    "password": "incorrect",
    "host": "localhost",
    "port": "5432"
}

def copy_table_data(cursor, table_name, file_path):
    try:
        with open(file_path, 'r') as f:
            cursor.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", f)
        print(f"Data copied to {table_name} table")
    except Exception as e:
        print(f"Error copying data to {table_name}: {e}")

def main():
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Copy data from CSV files to the respective tables
        for table, file_path in csv_files.items():
            copy_table_data(cursor, table, file_path)

        # Commit the transaction
        conn.commit()
        print("All data copied successfully")

    except Exception as e:
        print(f"Database error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
