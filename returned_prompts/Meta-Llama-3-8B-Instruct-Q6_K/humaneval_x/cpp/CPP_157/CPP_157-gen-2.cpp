Here is the correct solution:

```cpp
#include<stdio.h>
#include<math.h>
using namespace std;

bool right_angle_triangle(float a,float b,float c){
    if(a*a+b*b==c*c || a*a+c*c==b*b || b*b+c*c==a*a)
        return true;
    else
        return false;
}

int main() {
    printf("%d\n",right_angle_triangle(3,4,5)); // true
    printf("%d\n",right_angle_triangle(1,2,3)); // false
    return 0;
}
```

The function `right_angle_triangle(float a,float b,float c)` checks if the three sides `a`, `b`, `c` form a right-angled triangle. It uses the Pythagorean theorem to check if the square of the hypotenuse `c` is equal to the sum of the squares of the other two sides. If the condition is met, it returns `true`; otherwise, it returns `false`.

The main function calls the `right_angle_triangle` function with the sides of the triangles (3,4,5) and (1,2,3) and prints the results. The output will be:

```
1
0
```

This means that the triangle with sides 3, 4, 5 is a right-angled triangle, and the triangle with sides 1, 2, 3 is not.