    int count=0;
    for(int i:nums)
    {
        if(i>10)
        {
            int temp=i;
            int last_digit=temp%10;
            int first_digit=temp/10%10;
            if(last_digit%2!=0 && first_digit%2!=0)
            count++;
        }
    }
    return count;
}  