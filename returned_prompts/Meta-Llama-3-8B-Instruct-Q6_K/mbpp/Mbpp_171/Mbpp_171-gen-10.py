```
def perimeter_pentagon(side_length):
    return side_length * 5
```
This function takes the length of the side of a regular pentagon as input and returns the perimeter of the pentagon, which is the sum of the lengths of all its sides. Since a regular pentagon has five sides of equal length, the perimeter is simply the side length multiplied by 5. The unit test `assert perimeter_pentagon(5) == 25` ensures that the function works correctly, as the perimeter of a pentagon with a side length of 5 is indeed 25.