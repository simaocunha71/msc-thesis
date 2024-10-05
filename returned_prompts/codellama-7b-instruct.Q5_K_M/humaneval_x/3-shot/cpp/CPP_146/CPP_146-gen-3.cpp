    int count=0;
    for (int i=0;i<nums.size();i++)
    if (nums[i]>10)
    if (nums[i]%100000>10000)
    if (nums[i]%1000000000>100000000)
    if (nums[i]%1000000000000>100000000)
    if (nums[i]%1000000000000000>100000000)
    if (nums[i]%10000000000000000000>100000000)
    count+=1;
    return count;
}




