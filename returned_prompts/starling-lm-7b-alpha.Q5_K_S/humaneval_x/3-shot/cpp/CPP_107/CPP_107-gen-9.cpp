    vector<int> result;
    int i,count_odd=0,count_even=0;
    char chr;
    for (i=1;i<=n;i++)
    {
        chr=(char)(i+'0');
        if (chr==chr)
        {
        if (i%2==0)
            count_even+=1;
        else
            count_odd+=1;
        }
    }
    result.push_back(count_odd);
    result.push_back(count_even);
    return result;
}


