#include <iostream>
#include <cmath>
using namespace std;

bool is_simple_power(int x, int n) {
    if (x == 1) return true; // Special case for 1^k
    if (n == 1) return x == 1; // Special case for x^1
    
    int k = (int)log(x) / log(n);
    double result = pow(n, k);
    
    return result == (int)result && result == x;
}

int main() {
    cout << is_simple_power(1, 4) << endl; // true
    cout << is_simple_power(2, 2) << endl; // true
    cout << is_simple_power(8, 2) << endl; // true
    cout << is_simple_power(3, 2) << endl; // false
    cout << is_simple_power(3, 1) << endl; // false
    cout << is_simple_power(5, 3) << endl; // false
    return 0;
}
