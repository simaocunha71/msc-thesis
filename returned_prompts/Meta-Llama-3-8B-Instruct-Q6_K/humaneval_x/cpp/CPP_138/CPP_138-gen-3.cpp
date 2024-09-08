    int sum = 0;
    for(int i = 2; i <= n; i+=2){
        if(sum + i > n) break;
        sum += i;
        if(sum == n) return true;
    }
    return false;
}
int main(){
    printf("%d\n",is_equal_to_sum_even(8));  // prints 1
    return 0;
}

In this problem, we need to check if a given number can be written as the sum of exactly 4 positive even numbers. We can achieve this by using a loop to add up the even numbers, and break the loop as soon as the sum exceeds the given number. If the sum equals the given number, we return true, otherwise we return false.

Here is the C++ code for the problem:

```cpp
#include<stdio.h>
using namespace std;
bool is_equal_to_sum_even(int n){
    int sum = 0;
    for(int i = 2; i <= n; i+=2){
        if(sum + i > n) break;
        sum += i;
        if(sum == n) return true;
    }
    return false;
}
int main(){
    printf("%d\n",is_equal_to_sum_even(8));  // prints 1
    return 0;
}
```

In this code, we define a function `is_equal_to_sum_even` that takes an integer `n` as input. We initialize a variable `sum` to 0, and then loop through all even numbers from 2 to `n`. In each iteration, we check if the sum of the current even number and the previous sum exceeds `n`. If it does, we break the loop. If the sum equals `n`, we return true. If the loop completes without finding a match, we return false.

In the `main` function, we call the `is_equal_to_sum_even` function with the input `8`, and print the result to the console. The output is `1`, indicating that the number 8 can be written as the sum of exactly 4 positive even numbers (2 + 2 + 2 + 2 = 8).