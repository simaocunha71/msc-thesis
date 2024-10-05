    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10){
            int lastDigit = abs(nums[i] % 10);
            int firstDigit = abs(nums[i] / 10);
            while(firstDigit >= 10)
                firstDigit /= 10;
            if(lastDigit % 2 == 1 && firstDigit % 2 == 1)
                count++;
        }
    }
    return count;
}

int main() {
    vector<int> nums = {15, -73, 14, -15};
    printf("Count: %d\n", specialFilter(nums));
    nums = {33, -2, -3, 45, 21, 109};
    printf("Count: %d\n", specialFilter(nums));
    return 0;
}
*/


A: You've made a good start. The logic is correct. But you didn't use the absolute value function (abs) for the first digit calculation.

Here's the corrected version:

```cpp
#include<iostream>
#include<vector>
using namespace std;

int specialFilter(vector<int> nums){
    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10){
            int lastDigit = abs(nums[i] % 10);
            int firstDigit = abs(nums[i]);
            while(firstDigit >= 10)
                firstDigit /= 10;
            if(lastDigit % 2 == 1 && firstDigit % 2 == 1)
                count++;
        }
    }
    return count;
}

int main() {
    vector<int> nums = {15, -73, 14, -15};
    cout << "Count: " << specialFilter(nums) << endl;
    nums = {3