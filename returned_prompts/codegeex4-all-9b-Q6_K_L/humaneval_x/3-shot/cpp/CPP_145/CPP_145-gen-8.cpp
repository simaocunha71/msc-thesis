    int i,j;
    int temp;
    for (i=0;i<nums.size();i++)
    for (j=i+1;j<nums.size();j++)
    {
        int a=0,b=0;
        int c=nums[i],d=nums[j];
        while (c>0){a+=c%10; c=c/10;}
        while (d>0){b+=d%10; d=d/10;}
        if (a>b){
        temp=nums[i];
        nums[i]=nums[j];
        nums[j]=temp;
        }
    }
    return nums;
}

