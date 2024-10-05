    for (int i=0; i<nums.size(); i++) {
        int sum = 0;
        for (int j=0; j<nums[i]; j++) {
            sum += nums[i]%10;
            nums[i]/=10;
        }
        nums[i] = sum;
    }
    sort(nums.begin(), nums.end());
    return nums;
}

B:
    vector<int> order_by_points(vector<int> nums) {
        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            for (int j = 0; j < abs(nums[i]); j++) {
                sum += abs(nums[i]) % 10;
                nums[i] /= 10;
            }
            nums[i] = sum;
        }
        sort(nums.begin(), nums.end());
        return nums;
    }

C:
    vector<int> order_by_points(vector<int> nums) {
        int temp;
        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            for (int j = 0; j < abs(nums[i]); j++) {
                sum += abs(nums[i]) % 10;
                nums[i] /= 10;
            }
            nums[i] = sum;
        }
        sort(nums.begin(), nums.end());
        return nums;
    }

D:
    vector<int> order_by_points(vector<int> nums) {
        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            for (int j = 0; j < abs(nums[i]); j++) {
                sum += abs(nums[i]) % 10;
                nums[i] /= 10;
            }
            nums