#include <iostream>
#include <vector>
using namespace std;

int specialFilter(vector<int> nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] > 10 && (nums[i] % 10 % 2 == 1)) {
            count++;
        }
    }
    return count;
}

int main() {
    vector<int> test1 = {15, -73, 14, -15};
    vector<int> test2 = {33, -2, -3, 45, 21, 109};

    cout << specialFilter(test1) << endl; // Expected output: 1
    cout << specialFilter(test2) << endl; // Expected output: 2

    return 0;
}
B:
#include <iostream>
#include <vector>
using namespace std;

int specialFilter(vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        if (num > 10 && (num % 10 % 2 == 1)) {
            count++;
        }
    }
    return count;
}

int main() {
    vector<int> test1 = {15, -73, 14, -15};
    vector<int> test2 = {33, -2, -3, 45, 21, 109};

    cout << specialFilter(test1) << endl; // Expected output: 1
    cout << specialFilter(test2) << endl; // Expected output: 2

    return 0;
}
C:
#include <iostream>
#include <vector>
using namespace std;

int specialFilter(vector<int> nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] > 10 && (nums[i] % 10 % 2 == 1)) {
            count++;
        }
    }
    return count;
}

int main() {
    vector<int> test1 = {15, -73, 14, -15};
    vector<int> test2 = {33, -2, -3, 45, 21, 109};

    cout << specialFilter(test1) << endl; // Expected output: 1
    cout << specialFilter(test2) << endl; // Expected output: 2

    return 0;
}
D:
#include <