    if (n <= 0){
        return 0;
    }
    else if (n == 1){
        return 1;
    }
    else{
        return fib(n - 1) + fib(n - 2);
    }
}

int main(){
    int num;
    printf("Enter the position of Fibonacci sequence: ");
    scanf("%d", &num);
    printf("%dth Fibonacci number is: %d\n", num, fib(num));
    return 0;
}
```

In the code above, the `fib` function is recursive. It checks if the input number (n) is less than or equal to 0, if it is, it returns 0. If the input number is 1, it returns 1. For any other value, it calls itself with two arguments decremented by 1 and 2 respectively, sums them and returns the result. The main function takes user input and prints the nth Fibonacci number.

However, it's worth noting that this solution has a time complexity of O(2^n) due to the recursive nature of the function. This is not efficient for larger inputs. A more efficient solution would use dynamic programming to store previously computed values.

Here is an efficient version of the same code using dynamic programming:
```cpp
