    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Sum of numbers from 1 to %d is %d\n", n, sum_to_n(n));
    return 0;
}

S:
```c
#include<stdio.h>
using namespace std;

int sum_to_n(int n) {
    int sum = 0;
    for(int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Sum of numbers from 1 to %d is %d\n", n, sum_to_n(n));
    return 0;
}
```

This C program calculates the sum of numbers from 1 to n using the function sum_to_n(). It takes an integer input from the user and then prints the sum of numbers from 1 to that input number. The sum is calculated using a for loop that iterates from 1 to n and adds each number to the sum variable. The result is then returned and printed to the console. The main function takes the user's input and calls the sum_to_n() function with that input, then prints the result.