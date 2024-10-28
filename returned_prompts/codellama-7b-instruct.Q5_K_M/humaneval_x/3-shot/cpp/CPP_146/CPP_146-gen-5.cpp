    int count=0;
    for(int i=0;i<nums.size();i++)
    if (nums[i]>10)
    if ((nums[i]%10000>1000&&nums[i]%10000<100000)||(nums[i]%1000>100&&nums[i]%100<1000))
    count+=1;
    return count;
}



