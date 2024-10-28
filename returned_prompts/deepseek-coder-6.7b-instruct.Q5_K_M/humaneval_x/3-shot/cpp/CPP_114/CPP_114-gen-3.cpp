    long long sum = 0;
    long long min_sum = nums[0];
    for(auto i : nums){
        sum += i;
        if(sum < min_sum)
            min_sum = sum;
        if(sum > 0)
            sum = 0;
    }
    return min_sum;
}


