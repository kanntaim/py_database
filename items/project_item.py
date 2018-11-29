class ProjectItem:
    def __init__(self, project=None, distinct_tests=None):
        self.project = project
        self.distinct_tests = distinct_tests

    def __str__(self):
        return [self.project, self.distinct_tests].__str__()
