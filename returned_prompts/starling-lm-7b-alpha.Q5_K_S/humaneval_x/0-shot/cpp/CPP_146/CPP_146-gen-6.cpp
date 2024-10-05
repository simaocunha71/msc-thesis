
#include <vector>
#include <iostream>
using namespace std;

int specialFilter(vector<int> nums) {
    int cnt = 0;
    int temp;
    for (int i = 0; i < nums.size(); i++) {
        temp = nums[i];
        while (temp > 0) {
            if ((temp % 10) % 2 != 0 && (temp / 100) % 10 % 2 != 0) {
                cnt++;
                break;
            }
            temp /= 10;
        }
    }
    return cnt;
}

int main() {
    vector<int> nums = {33, -2, -3, 45, 21, 109};
    cout << specialFilter(nums) << endl;
    return 0;
}










































































































































