    int i,count=0;
    for (i=0;i<nums.size();i++)
    {
        int first_digit=nums[i]/100%10;
        int last_digit=nums[i]%10;
        if (first_digit%2==1 && last_digit%2==1 && nums[i]>10)
        count+=1;
    }
    return count;
}




