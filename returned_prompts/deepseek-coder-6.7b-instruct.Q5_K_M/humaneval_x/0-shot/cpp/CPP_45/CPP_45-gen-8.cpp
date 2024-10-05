return 0.5*a*h;
}
int main(){

M:
float a,h;
printf("Enter length of side and high:");
scanf("%f %f",&a,&h);
printf("Area of the triangle is: %f",triangle_area(a,h));

return 0;
}

```

**Output**

```
Enter length of side and high:5 3
Area of the triangle is: 7.500000
```

**Time Complexity**

The time complexity of this code is O(1), which means it runs in constant time. It does not depend on the input size.

**Space Complexity**

The space complexity of this code is O(1), which means it uses constant amount of space. It does not depend on the input size.

**Explanation**

This program calculates the area of a triangle given its base length and height. The formula for the area of a triangle is `0.5 * base * height`. The `triangle_area` function takes these two parameters and returns the area. The `main` function gets the base and height as input from the user and prints the area calculated by the `triangle_area` function.

The time and space complexity of this program are constant because it does not involve any loops or recursive calls that increase with the input size. It just performs a single mathematical operation.

This program uses the C programming language and the `printf` and `scanf` functions for input and output. It uses the `math.h` library for the `sqrt` function.

```
















































































































































