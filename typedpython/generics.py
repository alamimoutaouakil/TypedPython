from abc import abstractmethod

__all__ = ["GenericType"]


class GenericType:
    def __init__(self, value=None):
        self._attr_name = None
        self._value = None
        if value:
            self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self._validate(value):
            self._value = value
        else:
            # FIXME : return high level traceback
            raise TypeError(self._error_message)

    @abstractmethod
    def _validate(self, value):
        raise NotImplementedError()

    @property
    def _error_message(self):
        return "Wrong type for attribure {}".format(self._attr_name)


class GenericListType(GenericType):
    def _validate(self, value):
        subtype = self.subtype()
        if not isinstance(subtype, GenericType):
            raise TypeError("subtype method should return a GenericType instance.")
        return isinstance(value, list) and all(map(lambda x: subtype._validate(x), value))

    @abstractmethod
    def subtype(self):
        raise NotImplementedError()

