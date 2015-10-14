#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({r})".format(r=self.radius)

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

    doc = "largest distance between any two points on a circle"
