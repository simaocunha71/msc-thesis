    long long sum=0;
    for (auto i:lst)
    {
        if (i>0 && int(i)==i)
        {
            sum+=pow(i,2);
        }
    }
    return sum;
}   


