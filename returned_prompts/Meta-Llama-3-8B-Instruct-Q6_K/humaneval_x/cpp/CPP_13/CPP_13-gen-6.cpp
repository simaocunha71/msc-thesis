    int temp;
    if (b != 0) {
        temp = a;
        a = b;
        b = temp;
    }
    while (b != 0) {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("GCD of %d and %d is %d\n", a, b, greatest_common_divisor(a, b));
    return 0;
}

C++:
```
#include <iostream>
using namespace std;

int greatest_common_divisor(int a, int b) {
    if (b == 0)
        return a;
    else
        return greatest_common_divisor(b, a % b);
}

int main() {
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    cout << "GCD of " << a << " and " << b << " is " << greatest_common_divisor(a, b) << endl;
    return 0;
}
```
S:
The solution to the problem is to use the Euclidean algorithm, which is an efficient method for finding the greatest common divisor (GCD) of two integers.

The Euclidean algorithm works by repeatedly replacing `a` and `b` with `b` and `a % b`, respectively, until `b` becomes 0. At that point, `a` is the GCD of the original `a` and `b`.

Here is the C++ code that implements the Euclidean algorithm:
```
int greatest_common_divisor(int a, int b) {
    if (b == 0)
        return a;
    else
        return greatest_common_divisor(b, a % b);
}
```
This code uses a recursive function to find the GCD of `a` and `b`. The base case is when `b` is 0, in which case the GCD is simply `a`. Otherwise, the function calls itself with `b` and `a % b` as arguments.

To use this function, you can call it with two integers as arguments, like this:
```
int main() {
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    cout << "GCD of " << a <<