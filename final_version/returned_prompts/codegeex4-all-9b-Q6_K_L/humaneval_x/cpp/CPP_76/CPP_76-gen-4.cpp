#include <iostream>
using namespace std;

bool is_simple_power(int x, int n) {
    int p = 1;
    while (p <= x) {
        if (p == x) {
            return true;
        }
        p *= n;
    }
    return false;
}

int main() {
    cout << is_simple_power(1, 4) << endl;   // true
    cout << is_simple_power(2, 2) << endl;   // true
    cout << is_simple_power(8, 2) << endl;   // true
    cout << is_simple_power(3, 2) << endl;   // false
    cout << is_simple_power(3, 1) << endl;   // false
    cout << is_simple_power(5, 3) << endl;   // false
    return 0;
}