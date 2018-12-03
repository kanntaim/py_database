import datetime

from database import Database
from union_reporting import UnionReporting

database = Database(database='union_reporting', user='n.galeev')
date = (datetime.date(2015, 11, 7),)

rows = UnionReporting.get_tests_min_launch_time(database)
for row in rows:
    print(row, end='\n')
print('\n')

rows = UnionReporting.get_project_tests_count(database)
for row in rows:
    print(row, end='\n')
print('\n')

rows = UnionReporting.get_tests_since_time(database, date)
for row in rows:
    print(row, end='\n')
print('\n')

rows = UnionReporting.get_browser_test_launches_count(database)
for row in rows:
    print(row, end='\n')

database.close_connection()
