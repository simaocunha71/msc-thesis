#include <iostream>
using namespace std;

bool is_equal_to_sum_even(int n) {
    if (n <= 0) {
        return false;
    }
    if (n % 2 != 0) {
        return false;
    }
    if (n < 8) {
        return false;
    }
    if (n % 4 == 0) {
        return true;
    }
    return false;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    if (is_equal_to_sum_even(n)) {
        cout << n << " can be written as the sum of exactly 4 positive even numbers." << endl;
    } else {
        cout << n << " cannot be written as the sum of exactly 4 positive even numbers." << endl;
    }
    return 0;
}
