    int count=0;
    for (int i:nums)
    {
        if (i>10)
        {
            string str=to_string(i);
            if ((str[0]-'0')%2!=0 && (str.back()-'0')%2!=0)
                count++;
        }
    }
    return count;
}