    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        lst[i] = ceil(lst[i]);
        sum += pow(lst[i], 2);
    }
    return sum;
}

int main(){
    vector<float> lst = {1.4, 4.2, 0};
    printf("%d\n", sum_squares(lst));
    return 0;
}


A: You need to first round up each number in the array, then square the result and add them all together.

The ceil() function rounds up a number to the nearest integer, if the number is negative it is rounded down, if it's positive it's rounded up.

The pow() function takes two parameters, the base and the exponent, and returns the base raised to the power of the exponent.

In your code, you are doing the right thing by using ceil() to round up each number in the array, and pow() to square each number. You just need to add all the squared numbers together and return the result.

Here is the corrected code:

```cpp
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;

int sum_squares(vector<float> lst){
    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        lst[i] = ceil(lst[i]);
        sum += pow(lst[i], 2);
    }
    return sum;
}

int main(){
    vector<float> lst = {1.4, 4.2, 0};
    printf("%d\n", sum_squares(lst));  // prints: 29
    return 0;
}
```

This code will correctly solve the problem as described in the question.

Please note that in C++, you should use the `cmath` library for the `ceil()` and `pow()` functions, which are not part of the standard C library. This is why you need to include `#include<math.h>` in your