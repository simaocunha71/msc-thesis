    long long minSum = LONG_LONG_MAX;
    long long currentSum = 0;
    for(long long i = 0; i < nums.size(); i++){
        currentSum += nums[i];
        minSum = min(minSum, currentSum);
        if(currentSum > 0) currentSum = 0;
    }
    return minSum;
}

