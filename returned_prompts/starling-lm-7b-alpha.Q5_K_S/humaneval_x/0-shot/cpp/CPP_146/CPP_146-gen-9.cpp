#include <bits/stdc++.h>
using namespace std;

int specialFilter(vector<int> nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        int temp = nums[i];
        while (temp > 0) {
            if (temp % 10 % 2 == 1) {
                temp /= 10;
            } else {
                goto A;
            }
            count++;
        }
    }
    return count;
}

int main() {
    vector<int> nums = {33, -2, -3, 45, 21, 109};
    int count = specialFilter(nums);
    cout << "count: " << count << endl;
    return 0;
}

























































































