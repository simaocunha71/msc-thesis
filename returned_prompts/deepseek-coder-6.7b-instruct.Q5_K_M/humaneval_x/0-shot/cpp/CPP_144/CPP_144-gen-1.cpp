The problem can be solved using the concept of simplifying a fraction. A fraction can be simplified by dividing the numerator and the denominator by their greatest common divisor (GCD). The GCD of two numbers can be calculated using the Euclidean algorithm.

The function simplify is going to take two string representation of fractions and convert them to integer values. Then it will calculate the GCD of the numerators and denominators and divide them by the GCD. If the result is an integer, the function will return true, otherwise false.

Here is the code for the function simplify:

```cpp
bool simplify(string x, string y) {
    int num1 = stoi(x.substr(0, x.find('/')));
    int den1 = stoi(x.substr(x.find('/') + 1));
    int num2 = stoi(y.substr(0, y.find('/')));
    int den2 = stoi(y.substr(y.find('/') + 1));

    int gcd1 = __gcd(num1, den1);
    int gcd2 = __gcd(num2, den2);

    num1 /= gcd1;
    den1 /= gcd1;
    num2 /= gcd2;
    den2 /= gcd2;

    return (num1 * den2) % (den1 * num2) == 0;
}
```

In the function, stoi is used to convert the string representation of the numerator and denominator to integers. substr is used to extract the numerator and denominator from the string. find is used to find the position of '/' character. The __gcd function from the standard library is used to calculate the GCD of the numerators and denominators. After the division by the GCD, the function checks if the result is an integer by calculating the remainder