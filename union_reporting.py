from database import Database
from items.test_item import TestItem


class UnionReporting:
    @staticmethod
    def general_sql(ItemClass, query, params=None, **kwargs):
        db = Database(database="union_reporting", user='n.galeev')
        table = db.execute_select_query(query, params)
        tests = []
        for row in table:
            [*args] = row
            i = 0
            for key in kwargs.keys():
                kwargs[key] = args[i]
                i += 1
            tests.append(ItemClass(**kwargs))
        return tests

    @staticmethod
    def get_tests_min_launch_time():
        query = "select name, start_time " \
                "from test "
        return UnionReporting.general_sql(TestItem, query, test_name=None, execution_time=None)

    @staticmethod
    def get_tests_since_time(time):
        query = "select name, start_time " \
                "from test " \
                "where start_time>=%s"
        return UnionReporting.general_sql(TestItem, params=time, test_name=None, start_time=None)
