    int count=0;
    int i;
    for(i=0;i<nums.size();i++)
    {
        if(nums[i]>10)
        {
            int firstDigit=abs(nums[i]);
            while(firstDigit>=10)
            {
                firstDigit/=10;
            }
            int lastDigit=nums[i]%10;
            if(firstDigit%2==1 && lastDigit%2==1)
            count++;
        }
    }
    return count;
}

