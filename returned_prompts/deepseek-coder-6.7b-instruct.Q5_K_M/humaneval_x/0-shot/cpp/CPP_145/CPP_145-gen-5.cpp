    vector<int> result(nums.size());
    int i, j, max_idx;

    // One by one move boundary of unsorted subarray
    for (i = 0; i < nums.size()-1; i++)
    {
        // Find the maximum element in unsorted array
        max_idx = i;
        for (j = i+1; j < nums.size(); j++)
            if (abs(nums[j]) > abs(nums[max_idx]))
                max_idx = j;

        // Swap the found maximum element with the first element
        swap(nums[max_idx], nums[i]);
    }
    return nums;
}

int main() {
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int> res = order_by_points(nums);
    for (int i=0; i<res.size(); i++)
       printf("%d ", res[i]);
    return 0;
}

*/

//cplusplus/sorting/sum_of_digits.cpp
#include<stdio.h>
#include<vector>
using namespace std;

int sumOfDigits(int n) {
    int sum = 0;
    while (n != 0) {
        sum = sum + abs(n % 10);
        n = n / 10;
    }
    return sum;
}

vector<int> order_by_points(vector<int> nums) {
    // Sort nums based on the sum of its digits
    for (int i = 0; i < nums.size(); i++) {
        for (int j = 0; j < nums.size() - 1 - i; j++) {
            if (sumOfDigits(nums[j]) > sumOfDigits(nums[j + 1])) {
                int temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
            }
        }
   