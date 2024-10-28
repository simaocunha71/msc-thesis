if(a+b>c && b+c>a && c+a>b){
    float s = (a+b+c)/2;
    float area = sqrt(s*(s-a)*(s-b)*(s-c));
    return area;
}else{
    return -1;
}
}
int main(){
    float a,b,c;
    scanf("%f %f %f", &a, &b, &c);
    float res = triangle_area(a, b, c);
    printf("%f", res);
    return 0;
}
*/


A: The code you posted is a C++ version of the algorithm, but it's also C-style, i.e., it doesn't use any C++-specific features. If you want to use C++, you can make use of the std::sqrt function from the cmath library, and also use static_cast to convert the result to a float.

Here's the C++ version of the code:

```cpp
#include <cmath>

float triangle_area(float a, float b, float c){
    if(a + b > c && b + c > a && c + a > b){
        float s = (a + b + c) / 2;
        float area = std::sqrt(s * (s - a) * (s - b) * (s - c));
        return static_cast<float>(area);
    }else{
        return -1;
    }
}
```

This function takes the lengths of the three sides of a triangle as arguments, checks if the sides can form a valid triangle, and if so, calculates and returns the area of the triangle. If the sides can't form a valid triangle, it returns -1.

Please note that you should always include the necessary headers and use the correct function signatures according to your programming language and its standard library.

Also, when using the pow function in C++, you should pass two arguments to it: the number you want to raise to a power, and the power to which you want to raise it.

Finally, since the area of a triangle is a floating-point number, you should return a double from your function