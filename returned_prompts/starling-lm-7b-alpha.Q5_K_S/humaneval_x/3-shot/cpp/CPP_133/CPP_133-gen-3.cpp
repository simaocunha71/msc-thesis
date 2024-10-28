    int i;
    int sum=0;
    for (i=0;i<lst.size();i++)
    {
        lst[i]=int(ceil(lst[i]));
        sum+=lst[i]*lst[i];
    }
    return sum;
}




