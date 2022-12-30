#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is a reimplementation of `python_code.bad.open_close` module which
# abides by the open/close principle. You can see that it will be easy to
# extend the functionality of `AreaCalculator` in this module whereas it
# is not in `python_code.bad.open_close` module.

from abc import ABCMeta, abstractproperty

class Shape(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

class AreaCalculator(object):

    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area
        return total

# Note that if we want to extend the functionality of AreaCalculator to support calculating
# area of different shape, we only need to define new subtype of `Shape` and leave other code
# alone without modify them. That is the key of open/close principle.

def main():
    shapes = [Rectangle(1, 6), Rectangle(2, 3)]
    calculator = AreaCalculator(shapes)

    print("The total area is: "), calculator.total_area

if __name__ == '__main__':
    main()
