    int i,j;
    int temp;
    for (i=0;i<nums.size();i++)
    for (j=i+1;j<nums.size();j++)
    {
        if (abs(nums[i])<abs(nums[j]))
        {
            temp=nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
        }
    }
    return nums;
}


