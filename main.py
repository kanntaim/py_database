from database import *

db = Database("union_reporting")
query = "select browser, count(id)" \
        "from test" \
        "group by browser"
result = db.execute_query(query)
print(result)
