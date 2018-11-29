from database import *

db = Database(database="union_reporting", user='n.galeev')
queries = []

q
for query in queries:
    table = db.execute_select_query(query)
    print(table)
