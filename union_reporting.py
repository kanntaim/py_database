from database import Database
from items.browser_item import BrowserItem
from items.project_item import ProjectItem
from items.test_item import TestItem


class UnionReporting:
    @staticmethod
    def general_sql(ItemClass, query, params=None, **kwargs):
        db = Database(database='union_reporting', user='n.galeev')
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
        query = 'select p.name, t.name, min(timestampdiff(second, t.start, t.end)) ' \
                'from test t join project p on t.project_id = p.id ' \
                'group by p.name, t.name ' \
                'order by by p.name, t.name'
        return UnionReporting.general_sql(TestItem, query, project_name=None, test_name=None, execution_time=None)

    @staticmethod
    def get_tests_since_time(time):
        query = 'select p.name, t.name, t.start_time ' \
                'from test t join project p on t.project_id = p.id ' \
                'where t.start_time>=%s ' \
                'order by by p.name, t.name'
        return UnionReporting.general_sql(TestItem, query, params=time, test_name=None, start_time=None)

    @staticmethod
    def get_project_tests_count():
        query = 'select p.name, count(distinct t.name) ' \
                'from test t join project p on t.project_id = p.id ' \
                'group by p.name'
        return UnionReporting.general_sql(ProjectItem, query, project=None, distinct_tests=None)

    @staticmethod
    def get_browser_test_launches_count():
        query = 'select \'Chrome\', (select count(id) from test where browser = chrome ' \
                'union ' \
                'select \'Firefox\', (select count(id) from test where browser = firefox'
        return UnionReporting.general_sql(BrowserItem, query, browser=None, tests_launched=None)
