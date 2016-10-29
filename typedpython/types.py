from datetime import date

from typedpython.generics import GenericType

__all__ = ["String", "Date", "Double", "Integer", "Boolean"]


class TypedClass:
    def __setattr__(self, key, value):
        attr = self.__dict__.get(key)
        if isinstance(attr, GenericType):
            attr.value = value
        elif isinstance(value, GenericType):
            value._attr_name = key
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)
        if isinstance(attr, GenericType):
            return attr.value
        else:
            return attr


class String(GenericType):
    def _validate(self, value):
        return isinstance(value, str)

    @property
    def _error_message(self):
        return "Attribute {} should be of type str".format(self._attr_name)


class Double(GenericType):
    def _validate(self, value):
        return isinstance(value, float) or isinstance(value, int)

    @property
    def _error_message(self):
        return "Attribute {} should be of type double".format(self._attr_name)


class Integer(GenericType):
    def _validate(self, value):
        return isinstance(value, int)

    @property
    def _error_message(self):
        return "Attribute {} should be of type int".format(self._attr_name)


class Date(GenericType):
    def _validate(self, value):
        return isinstance(value, date)

    @property
    def _error_message(self):
        return "Attribute {} should be of type {}".format(self._attr_name, date.__name__)


class Boolean(GenericType):
    def _validate(self, value):
        return isinstance(value, bool)

    @property
    def _error_message(self):
        return "Attribute {} should be of type bool".format(self._attr_name)
