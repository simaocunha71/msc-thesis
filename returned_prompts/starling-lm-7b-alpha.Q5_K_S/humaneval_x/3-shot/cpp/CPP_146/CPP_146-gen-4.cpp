    int i,count=0;
    for (i=0;i<nums.size();i++)
    {
        string str=to_string(abs(nums[i]));
        if (str[0]%2!=0 && str[str.length()-1]%2!=0 && nums[i]>10)
        count+=1;
    }
    return count;
}


