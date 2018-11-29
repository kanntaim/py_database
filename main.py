from union_reporting import UnionReporting

rows = UnionReporting.get_tests_since_time('\'7.11.2015\'')
for row in rows:
    print(row, end='\n')
