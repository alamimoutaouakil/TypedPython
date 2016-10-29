# TypedPython

Typed pyhon is a package that will let you force type the attributes of your classes and check their integrity.

After defining your class, you can assign a value to the attributes of the class as you usually do in python, but this time it will be checked against the predefined type.


Here is an example of how to use is:

```python
from typedpython import types

class MyClass(types.TypedClass):
	def __init__(self):
    	self.mystring = types.String()
        self.myinteger = types.Integer()


obj = MyClass()
obj.mystring = "TypedPython is awesome"  # OK !
obj.myinteger = "This should be an integer"  # Will raise a TypeError

```