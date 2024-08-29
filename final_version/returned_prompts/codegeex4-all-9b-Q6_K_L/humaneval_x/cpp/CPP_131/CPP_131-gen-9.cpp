#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int digits(int n) {
        int result = 1;
        string s = to_string(n);
        for (int i = 0; i < s.length(); i++) {
            if (s[i] % 2 == 1) {
                result *= (s[i] - '0');
            }
        }
        if (result == 1) {
            return 0;
        }
        return result;
    }
};

int main() {
    Solution s;
    cout << s.digits(123456789) << endl; // 9
    cout << s.digits(2468) << endl; // 0
    cout << s.digits(13579) << endl; // 315
    cout << s.digits(1) << endl; // 1
    cout << s.digits(4) << endl; // 0
    cout << s.digits(235) << endl; // 15
    return 0;
}
B:
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int digits(int n) {
        int result = 1;
        vector<int> digits;
        while (n > 0) {
            digits.push_back(n % 10);
            n /= 10;
        }
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (digits[i] % 2 == 1) {
                result *= digits[i];
            }
        }
        if (result == 1) {
            return 0;
        }
        return result;
    }
};

int main() {
    Solution s;
    cout << s.digits(123456789) << endl; // 9
    cout << s.digits(2468) << endl; // 0
    cout << s.digits(13579) << endl; // 315
    cout << s.digits(1) << endl; // 1
    cout << s.digits(4) << endl; // 0
    cout << s.digits(235) << endl; // 15
    return 0;
}
C:
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int digits(int n) {
        int result = 1;
