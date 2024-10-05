    int count=0;
    for (int i=0;i<nums.size();i++)
    {
        if (nums[i]>10)
        {
            int temp=nums[i];
            if ((temp%100)%10==1||(temp%100)%10==3||(temp%100)%10==5||(temp%100)%10==7||(temp%100)%10==9)
            {
                count+=1;
            }
        }
    }
    return count;
}


