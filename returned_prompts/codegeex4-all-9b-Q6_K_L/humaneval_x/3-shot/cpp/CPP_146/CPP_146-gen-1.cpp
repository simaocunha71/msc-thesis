    int count=0;
    for (int i=0;i<nums.size();i++)
    {
        if (nums[i]>10 && abs(nums[i])%2==1 && abs(nums[i])%10%2==1)
            count+=1;
    }
    return count;
}

