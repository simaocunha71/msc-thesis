    int count=0;
    int i;
    for (i=0;i<nums.size();i++)
    {
        if (nums[i]>10)
        {
            if ((nums[i]%10)%2==1)
            count+=1;
        }
    }
    return count;
}


