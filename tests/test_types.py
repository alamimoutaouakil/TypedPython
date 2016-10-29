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

        self.string_list = types.StringList()
        self.double_list = types.DoubleList()
        self.integer_list = types.IntegerList()
        self.boolean_list = types.BooleanList()
        self.date_list = types.DateList()


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
        with self.assertRaises(TypeError):
            self.instance.string = 1
        with self.assertRaises(TypeError):
            self.instance.string = True

    def test_int(self):
        self.assertIsNone(self.instance.integer)
        self.instance.integer = 1
        self.assertEqual(self.instance.integer, 1)
        with self.assertRaises(TypeError):
            self.instance.integer = 1.2
        with self.assertRaises(TypeError):
            self.instance.integer = "This is a string"

    def test_double(self):
        self.assertIsNone(self.instance.double)
        self.instance.double = 1.2
        self.assertEqual(self.instance.double, 1.2)
        self.instance.double = 1
        self.assertEqual(self.instance.double, 1)
        with self.assertRaises(TypeError):
            self.instance.double = "This is a string"

    def test_date(self):
        self.assertIsNone(self.instance.date)
        today = datetime.date.today()
        self.instance.date = today
        self.assertEqual(self.instance.date, today)
        with self.assertRaises(TypeError):
            self.instance.date = "This is a string"
        with self.assertRaises(TypeError):
            self.instance.date = True
        with self.assertRaises(TypeError):
            self.instance.date = 1
        with self.assertRaises(TypeError):
            self.instance.date = 1.2

    def test_boolean(self):
        self.assertIsNone(self.instance.boolean)
        self.instance.boolean = True
        self.assertEqual(self.instance.boolean, True)
        with self.assertRaises(TypeError):
            self.instance.boolean = "This is a string"
        with self.assertRaises(TypeError):
            self.instance.boolean = 1
        with self.assertRaises(TypeError):
            self.instance.boolean = 1.2

    def test_string_list(self):
        self.assertIsNone(self.instance.string_list)
        self.instance.string_list = ["This is a string", "This is another string"]
        self.assertEqual(self.instance.string_list, ["This is a string", "This is another string"])
        with self.assertRaises(TypeError):
            self.instance.string_list = "This is a string"
        with self.assertRaises(TypeError):
            self.instance.string_list = 1
        with self.assertRaises(TypeError):
            self.instance.string_list = True

    def test_int_list(self):
        self.assertIsNone(self.instance.integer_list)
        self.instance.integer_list = [1, 2, 3]
        self.assertEqual(self.instance.integer_list, [1, 2, 3])
        with self.assertRaises(TypeError):
            self.instance.integer_list = 1.2
        with self.assertRaises(TypeError):
            self.instance.integer_list = "This is a string"
        with self.assertRaises(TypeError):
            self.instance.integer_list = 1

    def test_double_list(self):
        self.assertIsNone(self.instance.double_list)
        self.instance.double_list = [1.2, 1, 13, 2.1]
        self.assertEqual(self.instance.double_list, [1.2, 1, 13, 2.1])
        with self.assertRaises(TypeError):
            self.instance.double_list = "This is a string"
        with self.assertRaises(TypeError):
            self.instance.double_list = True
        with self.assertRaises(TypeError):
            self.instance.double_list = 1.2

    def test_date_list(self):
        self.assertIsNone(self.instance.date_list)
        today = datetime.date.today()
        self.instance.date_list = [today, today]
        self.assertEqual(self.instance.date_list, [today, today])
        with self.assertRaises(TypeError):
            self.instance.date_list = "This is a string"
        with self.assertRaises(TypeError):
            self.instance.date_list = True
        with self.assertRaises(TypeError):
            self.instance.date_list = 1
        with self.assertRaises(TypeError):
            self.instance.date_list = today

    def test_boolean_list(self):
        self.assertIsNone(self.instance.boolean_list)
        self.instance.boolean_list = [True, False]
        self.assertEqual(self.instance.boolean_list, [True, False])
        with self.assertRaises(TypeError):
            self.instance.boolean_list = "This is a string"
        with self.assertRaises(TypeError):
            self.instance.boolean_list = 1
        with self.assertRaises(TypeError):
            self.instance.boolean_list = [1.2, 1]
