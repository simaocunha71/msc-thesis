    int last_digit_a, last_digit_b, product;
    last_digit_a = abs(a) % 10;
    last_digit_b = abs(b) % 10;
    product = last_digit_a * last_digit_b;
    return product;
}

int main()
{
    int a, b, result;
    printf("Enter two numbers:");
    scanf("%d %d", &a, &b);
    result = multiply(a, b);
    printf("The product of the unit digits is: %d", result);
    return 0;
}

*/

#include <stdio.h>
#include <stdlib.h>

int multiply(int a, int b){
    int last_digit_a, last_digit_b, product;
    last_digit_a = abs(a) % 10;
    last_digit_b = abs(b) % 10;
    product = last_digit_a * last_digit_b;
    return product;
}

int main(){
    int a, b, result;
    printf("Enter two numbers:");
    scanf("%d %d", &a, &b);
    result = multiply(a, b);
    printf("The product of the unit digits is: %d", result);
    return 0;
}

//