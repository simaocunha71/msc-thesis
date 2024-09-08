    int int_part=static_cast<int>(number);
    float decimal_part=number-int_part;
    return decimal_part;
}

int main(){
    float number=3.5;
    float result=truncate_number(number);
    printf("Decimal part is: %f\n",result);
    return 0;
}

```

The function `truncate_number(float number)` takes a float number as an argument and returns the decimal part of the number. 

The integer part of the number is obtained by casting the number to an integer using the `static_cast<int>(number)` function. The decimal part is then calculated by subtracting the integer part from the original number. 

This is done by `float decimal_part=number-int_part;`. 

The function then returns the decimal part.

In the `main()` function, we take a float number `3.5` as an argument and call the `truncate_number()` function with this number. The result is then printed to the console using `printf()`. 

The output will be `Decimal part is: 0.500000`. 

This code will work correctly for any positive float number. 

The `static_cast<int>(number)` is used to convert the float number to an integer. This is a safe way to do this conversion, as it will truncate the decimal part and not round it. 

The `float decimal_part=number-int_part;` is a simple and efficient way to calculate the decimal part. 

The `return decimal_part;` statement returns the decimal part to the caller. 

The `printf()` function is used to print the result to the console. 

The `main()` function is the entry point of the program. It calls the `truncate_number()` function and prints the result. 

This code is easy to understand and will work correctly for any positive float number. 

It is a good example of how to decompose a float number into its integer and decimal parts. 

It is also a good example of how to use the `static_cast` function to convert a float number to an integer. 

It is a good example of how to use the `float` data type to represent a decimal number. 

It is a good example of how to use the `printf` function to print the result to the console. 

It is a good example of how to write a function that takes a float number as an argument and returns the decimal part of the number. 

It is a good example of how to write a main function that calls the `