    int i,j,temp,sum1,sum2;
    for(i=0;i<nums.size()-1;i++)
    {
        sum1=0;
        sum2=0;
        temp=abs(nums[i]);
        while(temp>0)
        {
            sum1+=temp%10;
            temp=temp/10;
        }
        temp=abs(nums[i+1]);
        while(temp>0)
        {
            sum2+=temp%10;
            temp=temp/10;
        }
        if(sum1>sum2)
        {
            temp=nums[i];
            nums[i]=nums[i+1];
            nums[i+1]=temp;
            i=-1;
        }
    }
    return nums;
}


