    int count=0;
    for (int num:nums)
    {
        if (num>10 && to_string(num)[0]%2!=0 && to_string(num)[to_string(num).length()-1]%2!=0)
        {
            count++;
        }
    }
    return count;
}