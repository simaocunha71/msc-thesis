    string result = "";
    int remainder;

    while(x > 0){
        remainder = x % base;
        x /= base;
        result = to_string(remainder) + result;
    }

    return result;
}

int main(){
    int x,base;
    printf("Enter number: ");
    scanf("%d",&x);
    printf("Enter base: ");
    scanf("%d",&base);
    printf("%s\n",change_base(x,base).c_str());

    return 0;
}
```

This is a C++ code that converts a given number `x` to a specified base. The number `x` is the input number and `base` is the base to which we want to convert the number `x`. The function `change_base` takes two parameters, `x` and `base`, and returns a string which is the base `base` representation of `x`. The string is built by repeatedly dividing `x` by `base` and appending the remainder to the beginning of the string until `x` becomes 0.

The `main` function just gets the input number and base from the user and prints the result of the `change_base` function.

The time complexity of this code is O(log(x)) because it performs a logarithmic number of operations to convert `x` to base `base`. The space complexity is also O(log(x)) because the string `result` can contain at most log(x) digits.

This code can handle bases less than 10. If you want to handle bases greater than 10, you can add a mapping from numbers 10 to 35 to characters A to Z.

This code works for all non-negative integers. If you want to handle negative numbers, you can add a special case to convert negative numbers to their two's complement representation.

This code uses the standard C++ library, so it should compile and run on any C++ compiler.

Note: This code does not handle edge cases such as negative numbers or bases greater than 10. If you need to handle these cases, you would need to modify the code accordingly.

Author: [GeeksforGeeks](https