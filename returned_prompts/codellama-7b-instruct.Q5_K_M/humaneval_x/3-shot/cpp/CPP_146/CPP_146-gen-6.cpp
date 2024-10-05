    int i;
    int counter=0;
    int temp;
    for (i=0;i<nums.size();i++)
    {
        temp=nums[i];
        if (temp>10)
        {
            if (temp%10==1 || temp%10==3 || temp%10==5 || temp%10==7 || temp%10==9)
            counter++;
        }
    }
    return counter;
}


