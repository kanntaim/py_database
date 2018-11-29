class TestItem:
    def __init__(self, project_name=None, test_name=None, execution_time=None, start_time=None):
        self.project_name = project_name
        self.test_name = test_name
        self.execution_time = execution_time
        self.start_time = start_time

    def __str__(self):
        return [self.project_name, self.test_name, self.execution_time, self.start_time].__str__()
