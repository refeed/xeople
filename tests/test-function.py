import unittest
import sys

sys.path.append('..')
import lib.xeoplefile as xeoplefile
import lib.xeoplerandom as xeoplerandom

class TestXeoplefileFunctions(unittest.TestCase):
    def test_parse(self):
        result = xeoplefile.parsefile('tests/test-name')
        self.assertIsInstance(result, list)
        self.assertEquals(len(result), 33)


class TestXeoplerandomFunctions(unittest.TestCase):
    def setUp(self):
        self.people_names = xeoplefile.parsefile('tests/test-name')
        # Make sure this is the right file that contains 33 people names
        self.assertEquals(len(self.people_names), 33)

    def test_random_select(self):
        result = xeoplerandom.random_select(self.people_names)
        self.assertIsInstance(result, str)
        # Make sure the result is a people from people_names
        self.assertTrue(result in self.people_names)

    def test_group_select(self):
        result = xeoplerandom.group_random_select(self.people_names, 3)
        self.assertIsInstance(result, list)
        # Make sure `group_random_select()` make 3 groups
        self.assertEquals(len(result), 3)
        # Make sure `group_random_select` divide peoples into 11
        self.assertEquals(len(result[0]), 11)
