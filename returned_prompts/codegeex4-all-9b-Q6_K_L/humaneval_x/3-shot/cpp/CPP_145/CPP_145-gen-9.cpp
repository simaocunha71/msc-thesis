    int i,j;
    int min=0;
    int temp;
    int sum=0;
    int sum2=0;
    for (i=0;i<nums.size();i++)
    {
        sum=0;
        for (j=0;j<nums[i];j++)
        if ((nums[i]%10)==1)
        sum+=1;
        if (nums[i]==1)
        sum=1;
        for (j=0;j<nums[i];j++)
        if ((nums[i]%10)==2)
        sum+=2;
        if (nums[i]==2)
        sum=2;
        for (j=0;j<nums[i];j++)
        if ((nums[i]%10)==3)
        sum+=3;
        if (nums[i]==3)
        sum=3;
        for (j=0;j<nums[i];j++)
        if ((nums[i]%10)==4)
        sum+=4;
        if (nums[i]==4)
        sum=4;
        for (j=0;j<nums[i];j++)
        if ((nums[i]%10)==5)
        sum+=5;
        if (nums[i]==5)
        sum=5;
        for (j=0;j<nums[i];j++)
        if ((nums[i]%10)==6)
        sum+=6;
        if (nums[i]==6)
        sum=6;
        for (j=0;j<nums[i];j++)
        if ((nums[i]%10)==7)
        sum+=7;
        if (nums[i]==7)
        sum=7;
        for (j=0;j<nums[i];j++)
        if ((nums[i]%10)==8)
        sum+=8;
        if (nums[i]==8)
        sum=8;
        for (j=0;j<nums[i];j++)
        if ((nums[i]%10)==9)
        sum+=9;
        if (nums[i]==9)
        sum=9;
        for (j=0;j<nums[i];j++)
        if ((nums[i]%10)==0)
        sum+=0;
        if (nums[i]==0)
        sum=0;
        for (j=0;j<nums.size();j++)
        {
            sum2=0;
            for (int k=0;k<nums[j];k++)
            if ((nums[j]%10)==1)
            sum2+=1;
            if (