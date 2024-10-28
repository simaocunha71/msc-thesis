    float integer_part = floor(number);
    float decimal_part = number - integer_part;
    return decimal_part;
}

int main()
{
    float number;
    printf("Enter a positive floating point number: ");
    scanf("%f", &number);
    printf("The decimal part of the number is: %f", truncate_number(number));
    return 0;
}
```

This C++ program takes a positive floating point number from the user and calls the function `truncate_number()` to return the decimal part of the number. The function uses the `floor()` function from the `math` library to get the integer part and subtracts it from the given number to get the decimal part.

Then it prints out the decimal part of the number.

When you run this program, it will ask for a positive floating point number. After you enter a number, it will print out the decimal part of the number.

For example, if you enter `3.5`, it will print `0.5`.

Please note that this program does not handle invalid inputs (like negative numbers). If you want to make the program more robust, you could add error checking to handle these cases.

Also, the `scanf` function is used here to read the floating point number from the user. It is important to note that the `%f` format specifier is used to read a floating point number.

This program can be compiled and run on any system that supports C++ and the math library.

```cpp
