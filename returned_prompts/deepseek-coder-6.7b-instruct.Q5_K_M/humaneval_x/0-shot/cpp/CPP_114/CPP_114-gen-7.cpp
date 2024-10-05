    long long sum = 0;
    long long min_sum = nums[0];
    for(long long i=0; i<nums.size(); i++){
        sum += nums[i];
        if(sum < min_sum)
            min_sum = sum;
        if(sum > 0)
            sum = 0;
    }
    return min_sum;
}


int main()
{
    vector<long long> nums = {-1, -2, -3};
    printf("%lld", minSubArraySum(nums));
    return 0;
}
```

## C++

```cpp
