    long long minSum=0;
    long long curSum=0;
    bool isNonNeg=true;
    for(long long num : nums){
        if(num>=0){
            isNonNeg=false;
            minSum+=num;
        }
    }
    if(isNonNeg) return 0;
    vector<long long> dp(nums.size(),0);
    dp[0]=nums[0];
    minSum=dp[0];
    for(long long i=1;i<nums.size();i++){
        dp[i]=min(nums[i],dp[i-1]+nums[i]);
        minSum=min(minSum,dp[i]);
    }
    return minSum;
}

int main(){
    printf("%lld\n",minSubArraySum({-1,-2,-3}));
    return 0;
}
```

### Python
```python
