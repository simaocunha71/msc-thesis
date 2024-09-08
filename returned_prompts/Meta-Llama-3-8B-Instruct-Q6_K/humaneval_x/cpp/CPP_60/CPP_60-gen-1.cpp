    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}

int main()
{
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("The sum of numbers from 1 to %d is %d\n", num, sum_to_n(num));
    return 0;
}  B:


C:
The correct code is:

```c
#include <stdio.h>

int sum_to_n(int n) {
    int sum = 0;
    for(int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("The sum of numbers from 1 to %d is %d\n", num, sum_to_n(num));
    return 0;
}
```

Explanation:
The code defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n`. The function uses a for loop to iterate from 1 to `n`, adding each number to a running sum. The sum is then returned.

In the `main` function, the user is prompted to enter a number. The `sum_to_n` function is called with the entered number as an argument, and the result is printed to the console.

Note that there is no need for a namespace declaration (`using namespace std;`) in this code, as it is a C program and does not use any C++ features. Also, the code does not contain any syntax errors or logical flaws.