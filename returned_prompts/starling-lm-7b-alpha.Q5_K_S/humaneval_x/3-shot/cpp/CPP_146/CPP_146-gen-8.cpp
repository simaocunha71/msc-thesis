    int i,count=0;
    for (i=0;i<nums.size();i++)
    {
        if (nums[i]>10 && (nums[i]%2==1) && (nums[i]/10)%10==3 && (nums[i]/100)%10==1)
        {
            count+=1;
        }
    }
    return count;
}

