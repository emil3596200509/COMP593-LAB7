"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

"""
import os
from faker import Faker # type: ignore
from datetime import datetime
import sqlite3

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    
    # TODO: Create function body
    conection = sqlite3.connect(db_path)
    cursor = conection.cursor()
    # Define an SQL query that creates a table named 'people'.
    # Each row in this table will hold information about a specific person.
    create_table ="""
    CREATE TABLE IF NOT EXISTS people
    (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        province TEXT NOT NULL,
        bio TEXT,
        age,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL
    );
    """
    cursor.execute(create_table)
    conection.commit()
    conection.close


def populate_people_table():
    # TODO: Create function body
    conection = sqlite3.connect(db_path)
    cursor = conection.cursor()
    
    fake = Faker("en_CA")

    for _ in range(200):
        name = fake.name()
        email = fake.email()
        address = fake.address()
        city = fake.city()
        province = fake.province()
        bio = fake.text()
        age = fake.random_int(min=10, max=100)
        created_at = datetime.now()
        updated_at = datetime.now()  

        add_people = """
        INSERT INTO people
        (
            name,
            email,
            address,
            city,
            province,
            bio,
            age,
            created_at,
            updated_at
        );
        """
        cursor.execute(add_people,(name, email, address, city, province, bio, age, created_at, updated_at))
    conection.commit()
    conection.close

if __name__ == '__main__':
   main()