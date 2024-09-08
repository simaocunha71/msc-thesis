    if (b == 0) {
        return a;
    } else {
        return greatest_common_divisor(b, a % b);
    }
}
int main() {
    int a, b;
    printf("Enter the first number: ");
    scanf("%d", &a);
    printf("Enter the second number: ");
    scanf("%d", &b);
    printf("Greatest common divisor of %d and %d is %d\n", a, b, greatest_common_divisor(a, b));
    return 0;
}
C:
#include <stdio.h>

int greatest_common_divisor(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return greatest_common_divisor(b, a % b);
    }
}

int main() {
    int a, b;
    printf("Enter the first number: ");
    scanf("%d", &a);
    printf("Enter the second number: ");
    scanf("%d", &b);
    printf("Greatest common divisor of %d and %d is %d\n", a, b, greatest_common_divisor(a, b));
    return 0;
}

R:
The recursive function greatest_common_divisor(a, b) will keep calling itself until b becomes 0. At that point, it will return the value of a, which is the greatest common divisor of a and b.

The base case is when b becomes 0, at which point the function returns a.

The recursive case is when b is not 0. In this case, the function calls itself with the arguments b and the remainder of a divided by b. This effectively reduces the problem size by one.

The function will continue to call itself until b becomes 0, at which point it will start returning values back up the call stack, until the original call to greatest_common_divisor(a, b) is reached. At that point, the function will return the greatest common divisor of a and b.

This is a classic example of a recursive algorithm, and it's a great way to solve the problem of finding the greatest common divisor of two integers.