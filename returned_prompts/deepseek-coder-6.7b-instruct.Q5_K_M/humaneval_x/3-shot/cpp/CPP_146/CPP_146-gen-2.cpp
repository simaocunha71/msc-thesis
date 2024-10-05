    int count=0;
    for(int i=0;i<nums.size();i++)
    {
        if(nums[i]>10)
        {
            int first = abs(nums[i]);
            while(first>=10)
            {
                first/=10;
            }
            int last = nums[i]%10;
            if(first%2==1 && last%2==1)
            count++;
        }
    }
    return count;
}


