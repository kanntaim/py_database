class BrowserItem:
    def __init__(self, browser=None, tests_launched=None):
        self.browser = browser
        self.tests_launched = tests_launched

    def __str__(self):
        return [self.browser, self.tests_launched].__str__()
