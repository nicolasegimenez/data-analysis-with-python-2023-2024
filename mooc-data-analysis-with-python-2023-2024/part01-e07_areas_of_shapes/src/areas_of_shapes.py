#!/usr/bin/env python3

import math
def triangle_area(base, height):
    "this function return the area of a triangle"
    return (base*height)/2
def rectangle_area(base, height):
    return(base*height)
def circle_area(r):
    return (math.pi*r**2)
    
def main():
    print(circle_area())
    # enter you solution here

if __name__ == "__main__":
    main()
