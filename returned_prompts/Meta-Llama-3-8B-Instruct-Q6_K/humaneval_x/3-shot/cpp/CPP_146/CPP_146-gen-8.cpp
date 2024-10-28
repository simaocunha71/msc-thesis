    int count=0;
    for (int i=0;i<nums.size();i++)
    {
        if (abs(nums[i])>10)
        {
            string str=to_string(abs(nums[i]));
            if (str[0]%2!=0 && str[str.length()-1]%2!=0)
                count++;
        }
    }
    return count;
}