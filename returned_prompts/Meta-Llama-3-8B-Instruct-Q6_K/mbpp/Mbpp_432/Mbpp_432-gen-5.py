The problem asks to create a function that calculates the median length of a trapezium. However, the problem does not provide the information about the lengths of the bases and the height of the trapezium. 

Fortunately, the unit test `assert median_trapezium(15,25,35)==20` gives us a hint about the input format. It seems that the function takes three arguments: the lengths of the two bases and the height of the trapezium.

Here is a Python solution for the problem:

```
def median_trapezium(base1, base2, height):
    semi_perimeter = (base1 + base2) / 2
    area = (semi_perimeter * (semi_perimeter - base1) * (semi_perimeter - base2)) ** 0.5
    return area
```

This function first calculates the semi-perimeter of the trapezium, then uses the formula for the area of a trapezium to calculate the median length. The median length is equal to the square root of the area. 

Please note that this solution assumes that the input values are valid and the trapezium exists in the given dimensions. In a real-world scenario, you would need to add error handling to deal with invalid inputs. 