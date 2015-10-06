#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def _init_(self, radius):
    """
    Initialize a circle with a given radius.
    """
    self.radius = radius
    self.diameter = 2*radius
    self.area = math.pi*radius**2

    def _get_d(self):
        return self._diameter
    def _set_d(self, value):
        self._diameter =value
        self.radius = value/2
        self.area = math.pi*self.radius**2
    def _del_d(self):
        del self._diameter
    diameter = property(_get_d, _set_d, _del_d)
    doc = "Largest distance between any two points on circle."

