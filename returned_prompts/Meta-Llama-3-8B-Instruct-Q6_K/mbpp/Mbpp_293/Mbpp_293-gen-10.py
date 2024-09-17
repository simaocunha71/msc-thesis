```
import math
def otherside_rightangle(a, b):
    return math.sqrt(a**2 + b**2)
```


This problem is asking you to write a function that finds the length of the third side of a right-angled triangle, given the lengths of the other two sides. 

The function should take two arguments, a and b, which are the lengths of the two sides. It should return the length of the third side, which is calculated using the Pythagorean theorem. 

The Pythagorean theorem states that the square of the length of the hypotenuse (the third side) is equal to the sum of the squares of the lengths of the other two sides. 

Here is the solution:
```
import math
def otherside_rightangle(a, b):
    return math.sqrt(a**2 + b**2)
```
This function uses the `math.sqrt` function to calculate the square root of the sum of the squares of the two sides, which gives the length of the hypotenuse. 

For example, if you call the function with the arguments 7 and 8, it will return the length of the hypotenuse of a right-angled triangle with sides of length 7 and 8, which is approximately 10.63. 

This is confirmed by the unit test:
```
assert otherside_rightangle(7,8)==10.63014581273465
```


This unit test checks that the function returns the correct length for the hypotenuse of a right-angled triangle with sides of length 7 and 8. 

The function can be used to find the length of the hypotenuse of any right-angled triangle, given the lengths of the other two sides. 

For example, if you know that one side of a right-angled triangle is 3 cm long and the other side is 4 cm long, you can use the function to calculate the length of the hypotenuse:
```
print(otherside_rightangle(3,4))
```
This would output the length of the hypotenuse, which is approximately 5.00. 

I hope this helps! Let me know if you have any questions. 

Note: The unit test is checking the result to 15 decimal places, so the function should be accurate to that level. The actual result may be slightly different due to the limitations of floating point arithmetic. 

Also, the function assumes that the input values are valid (i.e. they represent