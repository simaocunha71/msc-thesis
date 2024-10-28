
class Solution {
public:
    int minSubArraySum(vector<int>& nums) {
        int minSum = 0;
        int sum = 0;
        int i = 0;
        int j = 0;

        while (i < nums.size() && j < nums.size()) {
            sum += nums[j];
            j++;
            while (sum >= minSum) {
                minSum = sum;
                i = j - 1;
                sum -= nums[i];
            }
        }
        if (sum < minSum) {
            return sum;
        }
        return minSum;
    }
};