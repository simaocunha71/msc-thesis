    long long min_sum=LONG_LONG_MAX;
    long long current_sum=0;
    for (int i=0;i<nums.size();i++)
    {
        current_sum+=nums[i];
        if (current_sum<min_sum)
        min_sum=current_sum;
        if (current_sum>0)
        current_sum=0;
    }
    return min_sum;
}  // This function doesn't work correctly. It fails to return the minimum sum of a subarray. It always returns the minimum sum of the array itself. The problem is that it doesn't update the minimum sum when it encounters a negative number. It always adds the current sum to the minimum sum. It should update the minimum sum when it encounters a negative number. For example, for the input {-1, -2, -3}, it should return -6, but it returns LONG_LONG_MAX. The same problem occurs when the input array contains both positive and negative numbers. It should return the minimum sum of a subarray, not the minimum sum of the array itself.

