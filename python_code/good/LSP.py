#!/usr/bin/env python
# -*- coding: utf-8 -*-
# As we can see in `python_code.bad.LSP` module where a violation
# of LSP may lead to an unexpected behaviour of sub-types. In our 
# example, "is-a" relation can not directly applied to `Person` and 
# `Prisoner`. The cause is that these two classes "behave" differently.
# How to fix it? Maybe a better naming will do the trick:

class FreeMan(object):

    def __init__(self, position):
        self.position = position

    def walk_North(self, dist):
        self.position[1] += dist

    def walk_East(self, dist):
        self.position[0] += dist

# "is-a" relationship no longer holds since a `Prisoner` is not a `FreeMan`.
class Prisoner(object):
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        self.position = type(self).PRISON_LOCATION

def main():

    prisoner = Prisoner()
    print("The prisoner trying to walk to north by 10 and east by -3.")
    
    try:
        prisoner.walk_North(10)
        prisoner.walk_East(-3)
    except:
        pass
    
    print("The location of the prison: {}".format(prisoner.PRISON_LOCATION))
    print("The current position of the prisoner: {}".format(prisoner.position))

if __name__ == "__main__":
    main()