    if(a+b>c&&a+c>b&&b+c>a)
    {
        float s=(a+b+c)/2;
        float area=sqrt(s*(s-a)*(s-b)*(s-c));
        return round(area*100.0)/100.0;
    }
    else
    {
        return -1.0;
    }
}
int main()
{
    printf("%.2f\n",triangle_area(3,4,5));
    printf("%.2f\n",triangle_area(1,2,10));
    return 0;
}

R:
The problem is asking you to calculate the area of a triangle given three sides. The area of a triangle can be calculated using Heron's formula, which is:
```
A = sqrt(s * (s - a) * (s - b) * (s - c))
```
where `s` is the semi-perimeter of the triangle, which is the sum of the lengths of the three sides divided by 2.

Here is the solution in C++:
```cpp
#include <iostream>
#include <cmath>
using namespace std;

float triangle_area(float a, float b, float c) {
    // Check if the three sides can form a valid triangle
    if (a + b > c && a + c > b && b + c > a) {
        // Calculate the semi-perimeter
        float s = (a + b + c) / 2.0;
        // Calculate the area using Heron's formula
        float area = sqrt(s * (s - a) * (s - b) * (s - c));
        // Return the area rounded to 2 decimal places
        return round(area * 100.0) / 100.0;
    } else {
        // Return -1 if the three sides cannot form a valid triangle
        return -1.0;
    }
}

int main() {
    cout << fixed << setprecision(2);
    cout << triangle_area(3, 4, 5) << endl;
    cout << triangle_area(1, 2, 10) << endl;
    return 0;
}
```
This program first checks if the three sides can form a valid triangle by checking if the sum of any two sides is greater than the third side. If they can form a valid triangle, it calculates the semi-perimeter and the area using Heron's formula. If they cannot form a valid triangle, it returns -1