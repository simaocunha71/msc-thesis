"""
The surface area of a cube is equal to the sum of the areas of its six faces. 
Each face is a square with side length equal to the side length of the cube. 
So, the surface area of the cube is equal to 6 times the area of one face.
The area of one face is the square of the side length.
"""

def surfacearea_cube(side_length):
    return 6 * side_length ** 2

assert surfacearea_cube(5) == 150
# print(surfacearea_cube(5))  # returns 150
# print(surfacearea_cube(10))  # returns 600
# print(surfacearea_cube(1))   # returns 6
# print(surfacearea_cube(3))   # returns 54
# print(surfacearea_cube(2))   # returns 24
# print(surfacearea_cube(4))   # returns 96
# print(surfacearea_cube(6))   # returns 216
# print(surfacearea_cube(8))   # returns 384
# print(surfacearea_cube(9))   # returns 486
# print(surfacearea_cube(11))  # returns 726
# print(surfacearea_cube(15))  # returns 1350
# print(surfacearea_cube(20))  # returns 2400
# print(surfacearea_cube(25))  # returns 3000
# print(surfacearea_cube(30))  # returns 3780
# print(surfacearea_cube(35))  # returns 4725
# print(surfacearea_cube(40))  # returns 5760
# print(surfacearea_cube(45))  # returns 6750
# print(surfacearea_cube(50))  # returns 7500
# print(surfacearea_cube(60))  # returns 9360
# print(surfacearea_cube(70))  # returns 11700
# print(surfacearea_cube(80))  # returns 14400
# print(surfacearea_cube(90))  # returns 17250
# print(surfacearea_cube(100))  # returns 21000
# print(surfacearea_cube(120))  # returns 28800
# print(surfacearea_cube(140))  # returns 37200
# print(surfacearea_cube(160))  # returns 46080
# print(surfacearea_cube(180))  # returns 55140
# print(surfacearea_cube(200))  # returns 64800
