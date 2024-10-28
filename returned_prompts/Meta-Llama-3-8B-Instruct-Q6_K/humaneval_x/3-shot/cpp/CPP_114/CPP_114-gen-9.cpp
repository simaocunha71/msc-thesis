    long long min_sum=INT_MAX;
    long long current_sum=0;
    for (int i=0;i<nums.size();i++)
    {
        current_sum+=nums[i];
        min_sum=min(min_sum,current_sum);
        if (current_sum<0)
        {
            current_sum=0;
        }
    }
    return min_sum;
}
// or
long long minSubArraySum(vector<long long> nums){
    long long min_sum=INT_MAX;
    long long current_sum=0;
    for (int i=0;i<nums.size();i++)
    {
        current_sum+=nums[i];
        min_sum=min(min_sum,current_sum);
        if (current_sum>0)
        {
            current_sum=0;
        }
    }
    return min(min_sum,0);
}
// or
long long minSubArraySum(vector<long long> nums){
    long long min_sum=INT_MAX;
    for (int i=0;i<nums.size();i++)
    {
        long long current_sum=0;
        for (int j=i;j<nums.size();j++)
        {
            current_sum+=nums[j];
            min_sum=min(min_sum,current_sum);
        }
    }
    return min_sum;
} // this one has time complexity of O(n^2) while the other two are O(n) //


