    int i;
    int counter=0;
    int first_digit;
    int last_digit;
    for (i=0;i<nums.size();i++)
    if (nums[i]>10)
    {
        first_digit=abs(nums[i])/10;
        last_digit=abs(nums[i])%10;
        if (first_digit%2==1 && last_digit%2==1)
        counter+=1;
    }
    return counter;
}

