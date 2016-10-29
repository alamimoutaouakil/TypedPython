import datetime
import unittest

from typedpython import types


class TestClass(types.TypedClass):
    def __init__(self):
        self.string = types.String("This is a string")
        self.double = types.Double()
        self.integer = types.Integer()
        self.boolean = types.Boolean()
        self.date = types.Date()


class TestTypes(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.instance = TestClass()
        super().__init__(*args, **kwargs)

    def test_string(self):
        self.assertEqual(self.instance.string, "This is a string")
        self.instance.string = "This is another string"
        self.assertEqual(self.instance.string, "This is another string")
        with self.assertRaises(TypeError):
            self.instance.string = 1.2
            self.instance.string = 1
            self.instance.string = True

    def test_int(self):
        self.assertIsNone(self.instance.integer)
        self.instance.integer = 1
        self.assertEqual(self.instance.integer, 1)
        with self.assertRaises(TypeError):
            self.instance.integer = 1.2
            self.instance.integer = "This is a string"
            self.instance.integer = True

    def test_double(self):
        self.assertIsNone(self.instance.double)
        self.instance.double = 1.2
        self.assertEqual(self.instance.double, 1.2)
        self.instance.double = 1
        self.assertEqual(self.instance.double, 1)
        with self.assertRaises(TypeError):
            self.instance.double = "This is a string"
            self.instance.double = True

    def test_date(self):
        self.assertIsNone(self.instance.date)
        today = datetime.date.today()
        self.instance.date = today
        self.assertEqual(self.instance.date, today)
        with self.assertRaises(TypeError):
            self.instance.date = "This is a string"
            self.instance.date = True
            self.instance.date = 1
            self.instance.date = 1.2

    def test_boolean(self):
        self.assertIsNone(self.instance.boolean)
        self.instance.boolean = True
        self.assertEqual(self.instance.boolean, True)
        with self.assertRaises(TypeError):
            self.instance.boolean = "This is a string"
            self.instance.boolean = 1
            self.instance.boolean = 1.2
