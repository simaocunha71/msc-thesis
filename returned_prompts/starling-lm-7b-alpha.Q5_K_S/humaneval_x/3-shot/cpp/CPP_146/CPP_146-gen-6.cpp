    int count=0;
    int first,last;
    int i;
    for (i=0;i<nums.size();i++)
    {
        first=nums[i]/pow(10,nums[i]/10);
        last=nums[i]%10;
        if (nums[i]>10 && first%2==1 && last%2==1)
        {
            count+=1;
        }
    }
    return count;
}



