    for i := n; i > 0; i-- {
        if n % i == 0 {
            return i
        }
    }
    return 0
}



class Solution {
public:
    int largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> dp(nums.size());
        vector<int> parent(nums.size());
        int res = 0;
        for (int i = 0; i < nums.size(); ++i) {
            dp[i] = 1;
            parent[i] = -1;
            for (int j = 0; j < i; ++j) {
                if (nums[i] % nums[j] == 0 && dp[j]+1> dp[i]) {
                    dp[i] = dp[j] + 1;
                    parent[i] = j;
                }
            }
            res = max(res, dp[i]);
        }
        vector<int> resSet;
        for (int i = nums.size()-1; i>=0; i--) {
            if (parent[i] == -1 || resSet.size() == res) {
                break;
            }
            resSet.push_back(nums[i]);
        }
        return resSet.size();
    }
};







































































































































































