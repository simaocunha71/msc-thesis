```
#include <stdio.h>
using namespace std;

int fibfib(int n) {
    if (n <= 1) {
        return 0;
    } else if (n == 2) {
        return 1;
    } else {
        int a = 0, b = 0, c = 1;
        for (int i = 3; i <= n; i++) {
            int temp = a + b + c;
            a = b;
            b = c;
            c = temp;
        }
        return c;
    }
}

int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("The %dth element of the fibfib sequence is %d.\n", n, fibfib(n));
    return 0;
}
```

Explanation:

This code defines a function `fibfib` that calculates the `n-th` element of the fibfib sequence. The function uses a for loop to calculate the sequence up to the `n-th` element. The base cases for the function are when `n` is 0 or 1, in which case the function returns 0. When `n` is 2, the function returns 1.

The main function asks the user to input a value for `n`, then it calls the `fibfib` function with the input value and prints the result.

This code is efficient because it only calculates the necessary elements of the sequence and does not store all the elements in memory. The time complexity of this code is O(n), where n is the input value. The space complexity is O(1), because it only uses a constant