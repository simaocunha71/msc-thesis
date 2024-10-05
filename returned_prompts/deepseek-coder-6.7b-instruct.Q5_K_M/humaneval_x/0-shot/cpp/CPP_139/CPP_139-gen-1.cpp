    long long fact = 1;
    for(int i = n; i > 0; i--){
        fact = fact * i;
    }
    return fact;
}


int main(){
    int num;
    scanf("%d",&num);
    printf("%lld",special_factorial(num));
    return 0;
}
```

## 2. C++ Program to Calculate the Brazilian Factorial

```cpp
#include<iostream>
using namespace std;

long long special_factorial(int n){
    long long fact = 1;
    for(int i = n; i > 0; i--){
        fact = fact * i;
    }
    return fact;
}

int main(){
    int num;
    cin >> num;
    cout << special_factorial(num);
    return 0;
}
```

In the above code, we have defined a function `special_factorial(int n)` which calculates the factorial of a given number. We then use this function in the `main()` function to get the factorial of a number input by the user.

The `for` loop runs from `n` to `1`, and for each iteration, it multiplies the current value of `fact` by `i` (the current number in the loop). The result is stored back in `fact`. This continues until `i` is `1`, at which point `fact` contains the factorial of `n`. The function then returns this value. 

The function uses a `long long` to store the result because the factorial of large numbers can be very large. 

The `main()` function reads the number from the user, calls `special_factorial()` with this number as the argument, and then prints the result.

The `cin` and `cout` commands are used for reading from and writing to the console, respectively. `scanf()` and `printf()` could also be used in place of `cin` and `cout`.

Note: You need to compile the code before running it.

## 3. Python Program to Calculate the Brazilian Factorial

```python
def special_factorial(