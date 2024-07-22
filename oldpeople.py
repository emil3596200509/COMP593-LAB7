"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.
 
"""
import os
from create_db import db_path, script_dir
from pprint import pprint
import sqlite3
import pandas as pd

def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    # TODO: Create function body
    conection = sqlite3.connect(db_path)
    cursor = conection.cursor()
    cursor.execute('SELECT name, age FROM people Where age>=50')
    old_people = cursor.fetchall()
    conection.close()
    return old_people

def print_name_and_age(name_and_age_list):
    # TODO: Create function body
    for name, age in name_and_age_list:
        print(f"{name} is {age} years old.")

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    # TODO: Create function body
    df = pd.DataFrame(name_and_age_list, columns=["Name", "Age"])
    df.to_csv(csv_path, index=False)

if __name__ == '__main__':
   main()