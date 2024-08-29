#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isOdd(int num) {
    return num % 2 != 0;
}

bool isFirstAndLastDigitOdd(int num) {
    string strNum = to_string(num);
    char firstDigit = strNum[0];
    char lastDigit = strNum[strNum.length() - 1];
    return isOdd(firstDigit - '0') && isOdd(lastDigit - '0');
}

int specialFilter(vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        if (num > 10 && isFirstAndLastDigitOdd(num)) {
            count++;
        }
    }
    return count;
}

int main() {
    vector<int> nums1 = {15, -73, 14, -15};
    cout << "specialFilter({15, -73, 14, -15}) => " << specialFilter(nums1) << endl;

    vector<int> nums2 = {33, -2, -3, 45, 21, 109};
    cout << "specialFilter({33, -2, -3, 45, 21, 109}) => " << specialFilter(nums2) << endl;

    return 0;
}
B:
#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isFirstAndLastDigitOdd(int num) {
    string strNum = to_string(num);
    char firstDigit = strNum[0];
    char lastDigit = strNum[strNum.length() - 1];
    return (firstDigit == '1' || firstDigit == '3' || firstDigit == '5' || firstDigit == '7' || firstDigit == '9') &&
           (lastDigit == '1' || lastDigit == '3' || lastDigit == '5' || lastDigit == '7' || lastDigit == '9');
}

int specialFilter(vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        if (num > 10 && isFirstAndLastDigitOdd(num)) {
            count++;
        }
    }
    return count;
}

int main() {
    vector<int> nums1 = {15, -73, 14, -15};
    cout << "specialFilter({15, -73, 14, -15}) => " << specialFilter(nums1) << endl;

   