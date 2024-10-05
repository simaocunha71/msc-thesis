    long long sum=0,min_sum=0;
    for(int i=0;i<nums.size();i++){
        sum+=nums[i];
        if(sum<min_sum)
            min_sum=sum;
        if(nums[i]>0 && nums[i]>min_sum)
            min_sum=nums[i];
    }
    if(min_sum>0)
        return 0;
    else
        return abs(min_sum);
}

