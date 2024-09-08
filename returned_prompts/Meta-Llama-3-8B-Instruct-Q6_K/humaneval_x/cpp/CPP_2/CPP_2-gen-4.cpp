    int integer = floor(number);
    float decimal = number - integer;
    return decimal;
}
int main(){
    printf("%.2f",truncate_number(3.5));
    return 0;
}

C:
```c
#include <stdio.h>
#include <math.h>

float truncate_number(float number) {
    int integer = (int)floor(number);
    float decimal = number - integer;
    return decimal;
}

int main() {
    printf("%.2f", truncate_number(3.5));
    return 0;
}
```

This C code defines a function `truncate_number` that takes a floating-point number as input, calculates the integer part of the number using the `floor` function from the `math.h` library, and returns the decimal part of the number. The `main` function demonstrates the usage of the `truncate_number` function by calling it with the input `3.5` and printing the result with two decimal places using the `printf` function.

The output of the program will be `0.50`, which is the decimal part of the input `3.5`. The `%.2f` format specifier in the `printf` function is used to specify that the output should be a floating-point number with two decimal places.