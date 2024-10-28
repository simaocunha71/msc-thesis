    if(n <= 1)
        return false;
    if(n == 2)
        return true;
    if(n % 2 == 0)
        return false;
    for(long long i = 3; i * i <= n; i += 2)
        if(n % i == 0)
            return false;
    return true;
}
int main(){
    long long n;
    scanf("%lld",&n);
    if(is_prime(n)){
        printf("true");
    } else {
        printf("false");
    }
    return 0;
}
```

The function is_prime(long long n) is checking if the given number `n` is a prime number or not. If it is prime, it returns `true`, otherwise it returns `false`. 

The prime number check is performed by iterating from `3` to the square root of `n`. If `n` is divisible by any number in this range, it is not prime and the function returns `false`. If `n` is not divisible by any number in this range, it is prime and the function returns `true`.

Note: The function assumes that the input number is a positive integer. If the input number is `0` or a negative number, the function will return `false`.

Also note that the function uses a simple but efficient algorithm for checking primality: it checks divisibility only for odd numbers and stops at the square root of `n`. This reduces the number of checks needed, and makes the function much faster for large numbers.

The main function is just a driver function that takes an input from the user and prints out the result of the `is_prime` function.

If you want to use this function in a C++ program, you can include this code in your program. You would then call `is_prime` with the number you want to check as the argument.

This code uses the C++ `scanf` function to read the input number from the user, and `printf` to print the result. If you are not familiar with these functions, you can replace them with equivalent C++ statements.

The code uses the `<cstdio>` library for the `scanf` and `printf` functions, so make