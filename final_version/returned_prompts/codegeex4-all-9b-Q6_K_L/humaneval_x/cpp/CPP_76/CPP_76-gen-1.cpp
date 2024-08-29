```cpp
#include <cmath>
#include <iostream>

bool is_simple_power(int x, int n) {
    double logBaseN = log(x) / log(n);
    return logBaseN == floor(logBaseN);
}

int main() {
    // Test cases
    std::cout << std::boolalpha; // Print bools as true/false
    std::cout << "is_simple_power(1, 4): " << is_simple_power(1, 4) << std::endl; // true
    std::cout << "is_simple_power(2, 2): " << is_simple_power(2, 2) << std::endl; // true
    std::cout << "is_simple_power(8, 2): " << is_simple_power(8, 2) << std::endl; // true
    std::cout << "is_simple_power(3, 2): " << is_simple_power(3, 2) << std::endl; // false
    std::cout << "is_simple_power(3, 1): " << is_simple_power(3, 1) << std::endl; // false
    std::cout << "is_simple_power(5, 3): " << is_simple_power(5, 3) << std::endl; // false
    return 0;
}
```

B:
```cpp
#include <cmath>
#include <iostream>

bool is_simple_power(int x, int n) {
    if (x == 1) return true; // Special case: 1 is a simple power of any number
    double logBaseN = log(x) / log(n);
    return logBaseN == floor(logBaseN);
}

int main() {
    // Test cases
    std::cout << std::boolalpha; // Print bools as true/false
    std::cout << "is_simple_power(1, 4): " << is_simple_power(1, 4) << std::endl; // true
    std::cout << "is_simple_power(2, 2): " << is_simple_power(2, 2) << std::endl; // true
    std::cout << "is_simple_power(8, 2): " << is_simple_power(8, 2) << std::endl; // true
    std::cout << "is_simple_power(3, 2): " << is_simple_power(3,