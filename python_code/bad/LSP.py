#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The violation of LSP here is that a `Prisoner` is not a suitable 
# substitution of `Person` since they "behave" differently.
# Remember, the principle is that you should model your class according
# to their behavior rather than porperties. See "Circle-Ecllipse Problem"
# for detail.
import copy

class Person(object):

    def __init__(self, position):
        self.position = position

    def walk_North(self, dist):
        self.position[1] += dist

    def walk_East(self, dist):
        self.position[0] += dist

# `Prisoner` is a logicall natural extension of `Person`
# since they fulfill the "is-a" relation: a `Prisoner` is a `Person`.
# However, such extension violate LSP in this case.
class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False

# The issue here is that `Prisoner` inherite `walk_North` and `walk_East` methods
# from the `Person` which is not logically correct for the `Prisoner` class.

def main():
    prisoner = Prisoner()
    print "The prisoner trying to walk to north by 10 and east by -3."
    
    try:
        prisoner.walk_North(10)
        prisoner.walk_East(-3)
    except:
        pass
    
    print "The location of the prison: {}".format(prisoner.PRISON_LOCATION)
    print "The current position of the prisoner: {}".format(prisoner.position)

if __name__ == "__main__":
    main()