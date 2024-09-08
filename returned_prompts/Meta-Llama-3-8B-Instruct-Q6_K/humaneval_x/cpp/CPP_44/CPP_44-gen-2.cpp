    string res = "";
    while(x > 0){
        int r = x % base;
        res = (char)(r + '0') + res;
        x /= base;
    }
    return res;
}
int main(){
    printf("%s\n",change_base(8,3).c_str());
    printf("%s\n",change_base(8,2).c_str());
    printf("%s\n",change_base(7,2).c_str());
    return 0;
}
C:
The code above is a simple function in C++ that converts a number from one base to another. It uses a while loop to repeatedly divide the number by the base and append the remainder to the result string. The remainder is converted to a character by adding the ASCII value of '0' to it. The function then returns the result string.

Here's a step-by-step explanation of how the code works:

1. The function `change_base` takes two integer arguments `x` and `base`.
2. The result string `res` is initialized as an empty string.
3. The while loop continues as long as `x` is greater than 0.
4. Inside the loop, the remainder `r` of `x` divided by `base` is calculated using the modulo operator `%`.
5. The remainder `r` is converted to a character by adding the ASCII value of '0' to it. This is done using the expression `(char)(r + '0')`.
6. The character is prepended to the result string `res` using the `+` operator.
7. The value of `x` is updated by dividing it by `base` using the `/` operator.
8. The loop continues until `x` is 0.
9. The function returns the result string `res`.

The `main` function demonstrates the usage of the `change_base` function by calling it with different inputs and printing the results. The output of the program is:

```
22
1000
111
```
These are the results of converting the numbers 8, 8, and 7 to bases 3, 2, and 2, respectively.