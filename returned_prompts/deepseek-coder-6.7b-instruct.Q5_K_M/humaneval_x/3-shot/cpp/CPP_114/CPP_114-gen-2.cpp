    long long sum = 0, min_sum = 0;
    for(int i = 0; i < nums.size(); i++){
        sum += nums[i];
        if(sum < min_sum) min_sum = sum;
    }
    return min_sum;
}


