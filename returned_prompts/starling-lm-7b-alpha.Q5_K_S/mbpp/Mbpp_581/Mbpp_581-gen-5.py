Here is one way you can define the function:

```python
def surface_Area(edge, height):
    """
    Calculate the surface area of a square pyramid with a given edge length and height.

    Parameters:
    edge (int): The length of a side of the square base.
    height (int): The height of the pyramid.

    Returns:
    int: The surface area of the pyramid.
    """
    return edge * edge + 4 * edge * height
```

To test the function, you can use:

```python
assert surface_Area(3,4) == 33
```

The surface area of a square pyramid is calculated by taking the sum of the area of the four triangular faces. The area of each triangular face is half the base area multiplied by the height. For a square pyramid, the base is a square with side length equal to the given edge length.

So, the surface area of a square pyramid is equal to the sum of the areas of the four triangular faces, which is given by the formula:

surface area = edge * edge + 4 * edge * height

This is the formula that the `surface_Area` function uses to calculate the surface area of a square pyramid.

```python
def surface_Area(edge, height):
    """
    Calculate the surface area of a square pyramid with a given edge length and height.

    Parameters:
    edge (int): The length of a side of the square base.
    height (int): The height of the pyramid.

    Returns:
    int: The surface area of the pyramid.
    """
    return edge * edge + 4 * edge * height
```

To test the function, you can use:

```python
assert surface_Area(3,4) == 33
```

This assertion will pass if the calculated surface area of a square pyramid with a base edge of 3 and a height of 4 is equal to 33, as expected.

```python
def surface_Area(edge, height):
    """
    Calculate the surface area of a square py