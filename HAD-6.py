class MyClass(object):
    def __init__(self, x):
        self.x = x
        self._locked = True
    def __setattr__(self, name, value):
        if self.__dict__.get("_locked", False) and name == "x":
            raise AttributeError("MyClass does not allow assignment to .x member")
        self.__dict__[name] = value

>>> m = MyClass(3)
>>> m.x
3
>>> m.x = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in __setattr__
AttributeError: MyClass does not allow assignment to .x member