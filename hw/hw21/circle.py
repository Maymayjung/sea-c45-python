#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


def test_open_file():
    trigrams.test_open_file()


def test_read_lines():
    lines = trigrams.open_file()
    assert (len(lines) > 0)


class Circle(object):

    def _get_d(self):
        return self._diameter

    def _set_d(self, value):
        self._diameter = value
        self.radius = value / 2
        self.area = math.pi * self.radius ** 2

    def _del_d(self):
        del self._diameter
    diameter = property(_get_d, _set_d, _del_d)

    def __str__(self):
        return "Circle with radius: %.6f" % (self.radius)

    def __repr__(self):
        return "Circle(%d)" % (self.radius)

    def __add__(self, other):
        value = self.radius.__add__(other.radius)
        return Circle(value)

    def __eq__(self, other):
        return self.radius == other.radius

    def __mul__(self, other):
        value = self.radius.__mul__(other)
        return Circle(value)

    def __cmp__(self, other):
        if self.radius > other.radius:
            return 1
        elif self.radius < other.radius:
            return -1
        else:
            return 0
