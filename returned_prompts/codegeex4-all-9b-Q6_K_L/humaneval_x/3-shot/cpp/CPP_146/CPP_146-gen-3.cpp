    int i;
    int count=0;
    for (i=0;i<nums.size();i++)
    if (nums[i]>10 && (nums[i]%10)%2==1 && (nums[i]/10)%10%2==1)
    count+=1;
    return count;
}

