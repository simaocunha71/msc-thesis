    if(n <= 1) return 0;
    if(n == 2) return 1;
    int a = 0, b = 0, c = 1;
    for(int i = 3; i <= n; i++){
        int temp = a + b + c;
        a = b;
        b = c;
        c = temp;
    }
    return c;
}
int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The %d-th element of the fibfib sequence is %d.\n", n, fibfib(n));
    return 0;
}

Solution:
The problem asks to write a function to efficiently compute the n-th element of the fibfib number sequence. The fibfib sequence is defined as follows: fibfib(0) == 0, fibfib(1) == 0, fibfib(2) == 1, and fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n >= 3.

Here is the solution in C++:
```c
#include <stdio.h>
using namespace std;

int fibfib(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    int a = 0, b = 0, c = 1;
    for (int i = 3; i <= n; i++) {
        int temp = a + b + c;
        a = b;
        b = c;
        c = temp;
    }
    return c;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The %d-th element of the fibfib sequence is %d.\n", n, fibfib(n));
    return 0;
}
```
The function `fibfib` takes an integer `n` as input and returns the `n`-th element of the fibfib sequence. It uses a loop to calculate the sequence up to the `n`-th element.

In the `main` function, we prompt the user to enter a number, calculate the corresponding element of the fibfib sequence using the `fibfib` function, and print the result.

This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large