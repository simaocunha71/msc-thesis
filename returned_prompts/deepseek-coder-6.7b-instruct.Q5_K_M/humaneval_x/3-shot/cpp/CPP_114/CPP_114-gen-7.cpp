    long long sum = 0;
    long long min_sum = 0;
    for(int i=0;i<nums.size();i++){
        sum += nums[i];
        if(sum < min_sum)
            min_sum = sum;
        if(nums[i] > min_sum)
            min_sum = nums[i];
    }
    return min_sum;
}

