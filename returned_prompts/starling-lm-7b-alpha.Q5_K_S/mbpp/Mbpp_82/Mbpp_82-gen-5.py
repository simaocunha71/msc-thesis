"""
Here is a simple function to calculate the volume of a sphere:

def volume_sphere(radius):
    """
    Function to calculate the volume of a sphere.

    Parameters
    ----------
    radius : float
        The radius of the sphere.

    Returns
    -------
    volume : float
        The volume of the sphere.
    """
    return (4 / 3) * math.pi * radius ** 3

"""
Here is a simple function to calculate the volume of a sphere:

def volume_sphere(radius):
    """
    Function to calculate the volume of a sphere.

    Parameters
    ----------
    radius : float
        The radius of the sphere.

    Returns
    -------
    volume : float
        The volume of the sphere.
    """
    return (4 / 3) * math.pi * radius ** 3

This function takes the radius of a sphere as an input and returns the volume of the sphere. It uses the formula for the volume of a sphere, which is (4 / 3) * π * radius^3. The function uses the math.pi constant from the math module to calculate the value of π, and the ** operator to calculate the cube of the radius.

To use the function, you can call it with the radius of the sphere you want to calculate the volume for. For example, if you want to calculate the volume of a sphere with a radius of 10, you can call the function like this:

volume_sphere(10)

This will return the volume of the sphere, which you can then compare to the expected result using the math.isclose() function to check if the calculation is accurate within a specified tolerance.

In the provided assertion, the expected result is 4188.790204786391, and the relative tolerance is set to 0.001. This means that the calculated volume should be within 0.001 times the absolute value of the calculated volume from the expected result, or within 0.001 of the expected result itself, for the assertion to pass.

You can modify the radius parameter in the function call to calculate the volume of spheres with different radii, and use the math.isclose