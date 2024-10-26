import json
import yaml
import sqlite3
import os
import gzip
import itertools

# 1. Creating a sample SQLite database and table for demonstration
def init_database(db_name="example.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

# 2. Function to insert sample user data into the database
def insert_users(users, db_name="example.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    try:
        cursor.executemany(
            "INSERT INTO users (name, age, email) VALUES (?, ?, ?)", users
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# 3. Function to export user data from database to a JSON file
def export_to_json(db_name="example.db", output_file="users.json"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    # Transforming into dictionary format
    users_dict = [{"id": u[0], "name": u[1], "age": u[2], "email": u[3]} for u in users]

    # Writing to JSON file
    with open(output_file, "w") as f:
        json.dump(users_dict, f, indent=4)

    conn.close()

# 4. Function to create a YAML configuration file
def create_yaml_file(yaml_file="config.yaml"):
    config_data = {
        "database": {
            "name": "example.db",
            "table": "users"
        },
        "logging": {
            "level": "INFO",
            "file": "app.log"
        }
    }
    with open(yaml_file, "w") as f:
        yaml.dump(config_data, f)
    print(f"Created YAML configuration file: {yaml_file}")

# 5. Function to create a sample large text file
def create_large_file(file_path="large_file.txt"):
    with open(file_path, "w") as f:
        for i in range(1, 101):  # Create 100 lines for the example
            f.write(f"Line {i}: This is a sample line number {i}.\n")
    print(f"Created large text file: {file_path}")

# 6. Function to compress the large text file
def compress_large_file(input_file="large_file.txt", output_file="large_file.txt.gz"):
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            f_out.writelines(f_in)
    print(f"Compressed {input_file} to {output_file}")

# 7. Function to read a YAML file and display its contents
def read_yaml_file(yaml_file="config.yaml"):
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)
        print("YAML Data:", data)

# 8. Handling large files efficiently using iterators (Reading in chunks)
def process_large_file(file_path, chunk_size=1024):
    print(f"Processing large file: {file_path}")
    with gzip.open(file_path, 'rt') as f:  # Reading a compressed file
        for chunk in itertools.islice(f, chunk_size):
            print(chunk.strip())  # Process each line (or chunk) here

# 9. Main function to demonstrate all components
def main():
    # Step 1: Create a YAML configuration file
    create_yaml_file()
    print("----------------------------------------------------------------------------")
    # Step 2: Create a large text file
    create_large_file()
    print("----------------------------------------------------------------------------")
    # Step 3: Compress the large text file
    compress_large_file()
    print("----------------------------------------------------------------------------")
    # Step 4: Initialize database and insert users
    init_database()
    users = [("Alice", 25, "alice@example.com"),
             ("Bob", 30, "bob@example.com"),
             ("Charlie", 22, "charlie@example.com")]
    insert_users(users)
    print("----------------------------------------------------------------------------")
    # Step 5: Export database data to JSON file
    export_to_json()
    print("----------------------------------------------------------------------------")
    # Step 6: Read and print a YAML configuration file
    read_yaml_file()
    print("----------------------------------------------------------------------------")
    # Step 7: Efficiently process a large compressed file
    if os.path.exists("large_file.txt.gz"):
        process_large_file("large_file.txt.gz")
    else:
        print("Large file not found. Skipping this step.")

if __name__ == "__main__":
    main()
