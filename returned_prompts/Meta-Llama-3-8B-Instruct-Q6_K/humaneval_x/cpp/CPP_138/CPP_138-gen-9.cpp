    int sum = 0;
    for (int i = 2; i <= n; i += 2) {
        sum += i;
        if (sum == n) {
            return true;
        }
        if (sum > n) {
            return false;
        }
    }
    return false;
}

int main() {
    printf("%d\n", is_equal_to_sum_even(4));  // false
    printf("%d\n", is_equal_to_sum_even(6));  // false
    printf("%d\n", is_equal_to_sum_even(8));  // true
    return 0;
}

B:
#include <iostream>
#include <vector>
using namespace std;

bool is_equal_to_sum_even(int n) {
    for (int i = 2; i <= n; i += 2) {
        vector<int> numbers;
        int sum = 0;
        for (int j = 2; j <= i; j += 2) {
            numbers.push_back(j);
            sum += j;
            if (sum == n) {
                return true;
            }
            if (sum > n) {
                return false;
            }
        }
    }
    return false;
}

int main() {
    cout << is_equal_to_sum_even(4) << endl;   // 0
    cout << is_equal_to_sum_even(6) << endl;   // 0
    cout << is_equal_to_sum_even(8) << endl;   // 1
    return 0;
}
C:
#include <iostream>
#include <vector>
using namespace std;

bool is_equal_to_sum_even(int n) {
    for (int i = 2; i <= n; i += 2) {
        int sum = 0;
        for (int j = 2; j <= i; j += 2) {
            sum += j;
            if (sum == n) {
                return true;
            }
            if (sum > n) {
                break;
            }
        }
    }
    return false;
}

int main() {
    cout << is_equal_to_sum_even(4) << endl;   // 0
    cout << is_equal_to_sum_even(6) << endl;   // 0
    cout << is_equal_to_sum_even(8) << endl;   // 1
    return 0;
}

D:
#include <iostream>
#include <vector>
using namespace std;

bool