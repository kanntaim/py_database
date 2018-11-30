from union_reporting import UnionReporting
import datetime

date = datetime.date(2015, 11, 7)
rows = UnionReporting.get_tests_min_launch_time()
for row in rows:
    print(row, end='\n')
print('\n')

rows = UnionReporting.get_project_tests_count()
for row in rows:
    print(row, end='\n')
print('\n')

rows = UnionReporting.get_tests_since_time(date)
for row in rows:
    print(row, end='\n')
print('\n')

rows = UnionReporting.get_browser_test_launches_count()
for row in rows:
    print(row, end='\n')
