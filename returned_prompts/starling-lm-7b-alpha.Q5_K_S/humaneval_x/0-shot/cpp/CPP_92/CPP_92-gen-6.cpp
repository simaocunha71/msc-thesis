I understand that the question is asking for a function that takes three numbers and returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers. It should return false in any other cases.

To solve this problem, we can use the following approach:

1. Check if all the numbers are integers by comparing them with their floor values. If any of them is not an integer, return false.
2. If all the numbers are integers, check if the sum of any two numbers is equal to the third number. If it is, return true. Otherwise, return false.

Here's the code implementation of the solution:

```cpp
#include<stdio.h>
#include<math.h>
using namespace std;

bool any_int(float a, float b, float c) {
    if (a == floor(a) && b == floor(b) && c == floor(c)) {
        if (a + b == c || a + c == b || b + c == a) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

int main() {
    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);
    if (any_int(a, b, c)) {
        printf("true");
    } else {
        printf("false");
    }
    return 0;
}
```
