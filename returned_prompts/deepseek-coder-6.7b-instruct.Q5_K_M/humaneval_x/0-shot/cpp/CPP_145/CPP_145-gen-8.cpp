vector<int> order_by_points(vector<int> nums){
    vector<pair<int, int>> nums_with_sums;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int num = abs(nums[i]);
        while(num){
            sum += num%10;
            num /= 10;
        }
        nums_with_sums.push_back({sum, i});
    }

    sort(nums_with_sums.begin(), nums_with_sums.end());

    vector<int> result(nums.size());
    for(int i = 0; i < nums.size(); i++){
        result[i] = nums[nums_with_sums[i].second];
    }
    return result;
}

// Test Cases
void test_order_by_points(){
    assert(order_by_points({1, 11,