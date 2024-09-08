    long long minSum = nums[0];
    for(int i = 0; i < nums.size(); i++){
        long long sum = 0;
        for(int j = i; j < nums.size(); j++){
            sum += nums[j];
            if(sum < minSum){
                minSum = sum;
            }
        }
    }
    return minSum;
}

int main(){
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    printf("%lld\n", minSubArraySum(nums)); // 1
    nums = {-1, -2, -3};
    printf("%lld\n", minSubArraySum(nums)); // -6
    return 0;
}
E:
/*
This code is correct and works as expected. It calculates the minimum sum of any non-empty sub-vector of nums. The time complexity of the code is O(n^2) which is acceptable for the given problem constraints. The space complexity is O(1) as no extra space is used.
*/