    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Sum of numbers from 1 to %d is: %d\n", n, sum_to_n(n));
    return 0;
}

C++:
```c
#include <iostream>

using namespace std;

int sum_to_n(int n) {
    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Sum of numbers from 1 to " << n << " is: " << sum_to_n(n) << endl;
    return 0;
}
```

Explanation:
This C++ program calculates the sum of numbers from 1 to n and prints the result. The function `sum_to_n` takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The `main` function prompts the user to enter a number, calculates the sum using the `sum_to_n` function, and prints the result.

The `sum_to_n` function uses a for loop to iterate from 1 to `n` and add each number to the `sum` variable. The `main` function uses `cout` to print a message asking the user to enter a number, reads the input using `cin`, calculates the sum using `sum_to_n`, and prints the result using `cout`. The `endl` at the end of the `cout` statement is used to insert a new line after printing the result.

The program uses the `using namespace std;` directive to bring the standard namespace into scope, which allows us to use `cout`, `cin`, and other standard library functions without qualifying them with the `std::` prefix. The `#include <iostream>` directive is used to include the iostream header file, which provides input/output functions such as `cout` and `cin`. The `#include <cstdio>` directive is not necessary in this program, as we are not using any functions from the cstdio header file. The `using namespace std;` directive is not necessary if we want to avoid using the `std::` prefix, we