/*
Write a program to check whether a given number is an automorphic number.
An automorphic number is a number whose square of any digit is equal to the number.
For example, 153 is an automorphic number because 1^2 + 5^2 + 3^2 = 153
*/
#include <stdio.h>
int main()
{
    int n, r, s = 0, temp;
    printf("Enter a number: ");
    scanf("%d", &n);
    temp = n;
    while (n > 0)
    {
        r = n % 10;
        s = s + (r * r);
        n = n / 10;
    }
    if (s == temp)
        printf("%d is an automorphic number.", temp);
    else
        printf("%d is not an automorphic number.", temp);
    return 0;
}
