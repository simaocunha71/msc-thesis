    int i,count=0;
    for (i=0;i<nums.size();i++)
    {
        int num=nums[i];
        if (num>10 && (num/10)%2==1 && num%10==1)
        {
            count+=1;
        }
    }
    return count;
}



