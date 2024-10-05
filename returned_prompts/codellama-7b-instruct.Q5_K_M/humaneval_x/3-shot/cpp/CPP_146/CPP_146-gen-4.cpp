    int count=0;
    int len=nums.size();
    int i;
    for (i=0;i<len;i++)
    if ((nums[i]>10)&&((nums[i]/10)%2!=0)&&(nums[i]%10)%2!=0)
    count+=1;
    return count;
}



