    int i, count=0, num;
    for (i=0;i<nums.size();i++)
    {
        num=nums[i];
        if (num>10)
        {
            int first_digit=num/10;
            int last_digit=num%10;
            if ((first_digit%2==1)&&(last_digit%2==1))
            count+=1;
        }
    }
    return count;
}




