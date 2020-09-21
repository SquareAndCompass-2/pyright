# This sample verifies that enums are iterable.

import enum
from typing import Type


class Color(enum.Enum):
    RED = enum.auto()
    GREEN = enum.auto()


class Foo:
    _foo: Type[enum.Enum]

    def __init__(self):
        self._foo = Color

    def _print_foo(self):
        for f in self._foo:
            print(f)


