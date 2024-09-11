"""
import math

def lateralsurface_cone(r,h):
    """
    Finds the lateral surface area of a cone

    Parameters
    ----------
    r : int or float
        The radius of the cone
    h : int or float
        The height of the cone

    Returns
    -------
    float
        The lateral surface area of the cone
    """
    return math.pi * r * (math.sqrt(h*h+r*r))

if __name__ == "__main__":
    print(lateralsurface_cone(5,12))
"""

In this code, we first import the math module, which will be necessary for our calculations. We define a function called lateralsurface_cone, which takes in two parameters: r (the radius of the cone) and h (the height of the cone). The function then uses the formula for the lateral surface area of a cone, which is pi * r * sqrt(h^2 + r^2), to calculate the lateral surface area of the cone. Finally, we test the function by passing in the values 5 and 12 for r and h, respectively, and printing the result. The expected output is 204.20352248333654, which is the lateral surface area of the cone with radius 5 and height 12.

To use this code, simply copy and paste it into a Python file or interpreter, and then call the lateralsurface_cone function with your desired values for r and h. The function will return the lateral surface area of the cone, which you can then use in your calculations or display to the user.

Note that the math.sqrt function is used to calculate the square root of a number, and the math.pi constant is used to represent the value of pi (approximately 3.14159). These functions are part of the math module, which provides various mathematical operations and constants.

Overall, this code provides an efficient and accurate way to calculate the lateral surface area of a cone, and can be easily integrated into a program or script to perform calculations involving cones.

"""

def lateralsurface_cone(r,h):
   