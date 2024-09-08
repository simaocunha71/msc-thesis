#include <iostream>
#include <vector>
using namespace std;

bool is_equal_to_sum_even(int n){
    if (n < 8 || n % 2 != 0) {
        return false;
    }
    vector<int> nums;
    for (int i = 2; i <= n; i += 2) {
        nums.push_back(i);
    }
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            for (int k = j + 1; k < nums.size(); k++) {
                for (int l = k + 1; l < nums.size(); l++) {
                    if (nums[i] + nums[j] + nums[k] + nums[l] == n) {
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

int main() {
    cout << is_equal_to_sum_even(4) << endl;  // false
    cout << is_equal_to_sum_even(6) << endl;  // false
    cout << is_equal_to_sum_even(8) << endl;  // true
    return 0;
}

B:
#include <iostream>
#include <vector>
using namespace std;

bool is_equal_to_sum_even(int n){
    if (n < 8 || n % 2 != 0) {
        return false;
    }
    vector<int> nums;
    for (int i = 2; i <= n; i += 2) {
        nums.push_back(i);
    }
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            for (int k = j + 1; k < nums.size(); k++) {
                for (int l = k + 1; l < nums.size(); l++) {
                    if (nums[i] + nums[j] + nums[k] + nums[l] == n) {
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

int main() {
    cout << is_equal_to_sum_even(4) << endl;  // false
    cout << is_equal_to_sum_even(6) << endl;  // false
    cout << is_equal_to_sum_even(8) << endl;  // true
    return 0