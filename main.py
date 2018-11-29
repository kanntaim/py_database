from union_reporting import UnionReporting

rows = UnionReporting.get_tests_min_launch_time()
for row in rows:
    print(row, end='\n')
