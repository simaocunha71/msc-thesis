The provided C++ code checks if one of the input numbers is equal to the sum of the other two. The code returns true if this condition is met and all numbers are integers. Otherwise, it returns false.

Here is the code:

```cpp
#include<stdio.h>
#include<math.h>
using namespace std;
bool any_int(float a,float b,float c){
    if(a == b+c || b == a+c || c == a+b)
        return true;
    else
        return false;
}

int main(){
    printf("%d\n",any_int(5, 2, 7)); // ➞ true
    printf("%d\n",any_int(3, 2, 2)); // ➞ false
    printf("%d\n",any_int(3, -2, 1)); // ➞ true
    printf("%d\n",any_int(3.6, -2.2, 2)); // ➞ false
    return 0;
}
```

Explanation:

1. The function `any_int(float a,float b,float c)` is defined to take three floating-point numbers as input.
2. Inside the function, it checks if any of the following conditions are met:
   - `a` is equal to the sum of `b` and `c`.
   - `b` is equal to the sum of `a` and `c`.
   - `c` is equal to the sum of `a` and `b`.
3. If any of these conditions are met, the function returns `true`. Otherwise, it returns `false`.
4. In the `main` function, the `any_int` function is called with different sets of input numbers. The output of the program is the return value of the `any_int` function for each set of input numbers.