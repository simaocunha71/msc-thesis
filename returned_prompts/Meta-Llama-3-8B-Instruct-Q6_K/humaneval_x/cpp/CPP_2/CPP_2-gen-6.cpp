    // integer part
    float int_part = floor(number);
    // decimal part
    float dec_part = number - int_part;
    return dec_part;
}

int main() {
    printf("%f", truncate_number(3.5));
    return 0;
}

Explanation:
In the given problem, we are asked to write a function `truncate_number` that takes a floating point number as an argument and returns the decimal part of the number.

The decimal part of a floating point number can be obtained by subtracting the integer part from the number. The integer part can be obtained by using the `floor` function from the `<math.h>` library.

Here is the implementation of the `truncate_number` function in C++:
```cpp
float truncate_number(float number) {
    float int_part = floor(number);
    float dec_part = number - int_part;
    return dec_part;
}
```
In the `main` function, we call the `truncate_number` function with the argument `3.5` and print the result using `printf` function.

The output of the program will be `0.5`, which is the decimal part of the number `3.5`.