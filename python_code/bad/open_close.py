#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Think about what will happen if you want to extend the class to calculate
# the area of different shape? What would you do with the code in the property
# `total_area` of class `AreaCalculator`?

class Rectangle(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

class AreaCalculator(object):

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.width * shape.height

        return total

def main():
    shapes = [Rectangle(2, 3), Rectangle(1, 6)]
    calculator = AreaCalculator(shapes)
    print("The total area is: "), calculator.total_area

if __name__ == '__main__':

    main()
