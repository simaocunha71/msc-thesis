    int i,count=0;
    for (i=0;i<nums.size();i++)
    {
        string str=to_string(nums[i]);
        int first=str[0]-'0';
        int last=str[str.length()-1]-'0';
        if (first%2!=0 && last%2!=0 && nums[i]>10)
        {
            count+=1;
        }
    }
    return count;
}



