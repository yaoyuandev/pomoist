from unittest import TestCase
import todoist

class Test(TestCase):
    def test_label(self):
        todoist.label("now", "")

