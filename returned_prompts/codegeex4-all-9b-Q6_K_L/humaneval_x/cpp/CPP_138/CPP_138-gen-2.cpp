#include <iostream>
#include <vector>
using namespace std;

bool is_equal_to_sum_even(int n) {
    for (int i = 2; i <= n; i += 2) {
        if (n - i >= 0 && (n - i) % 2 == 0) {
            for (int j = i + 2; j <= n - i; j += 2) {
                if ((n - i - j) % 2 == 0 && n - i - j >= 0) {
                    for (int k = j + 2; k <= n - i - j; k += 2) {
                        if ((n - i - j - k) % 2 == 0 && n - i - j - k >= 0) {
                            for (int l = k + 2; l <= n - i - j - k; l += 2) {
                                if ((n - i - j - k - l) % 2 == 0 && n - i - j - k - l >= 0) {
 return true;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return false;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    if (is_equal_to_sum_even(n)) {
        cout << "The number can be written as the sum of exactly 4 positive even numbers." << endl;
    } else {
        cout << "The number cannot be written as the sum of exactly 4 positive even numbers." << endl;
    }
    return 0;
}

B:
#include <iostream>
#include <vector>
using namespace std;

bool is_equal_to_sum_even(int n) {
    int sum = 0;
    for (int i = 0; i < 4; i++) {
        sum += 2;
    }
    return (n == sum);
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    if (is_equal_to_sum_even(n)) {
        cout << "The number can be written as the sum of exactly 4 positive even numbers." << endl;
    } else {
        cout << "The number cannot be written as the sum of exactly 4 positive even numbers." << endl;
    }
    return 0;
}

C:
#include <iostream>
#include <vector>
using namespace