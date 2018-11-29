from database import Database
from tables.items.test_item import TestItem
from tables.items.browser_item import BrowserItem
from tables.items.project_item import ProjectItem


class UnionReporting:
    @staticmethod
    def general_sql(self, ItemClass, query, params=None, **kwargs):
        db = Database(database="union_reporting", user='n.galeev')
        table = db.execute_select_query(query, params)
        tests = []
        for row in table:
            [*args] = row
            i = 0
            for key in kwargs.keys():
                kwargs[key] = args[i]
            tests.append(ItemClass(**kwargs))
        return tests

    @staticmethod
    def get_tests_min_launch_time(self):
        query = "select browser, count(id) " \
            "from test " \
            "group by browser"
        self.general_sql(TestItem, query, project_name=None, test_name=None, execution_time=None)

    @staticmethod
    def get_tests_since_time(self, time):
        query = ""
        self.general_sql(TestItem, params=time, project_name=None, test_name=None, start_time=None)
