    int i,sum=0;
    for (i=0;i<lst.size();i++)
    {
        if (i%3==0)
        lst[i]=lst[i]*lst[i];
        if (i%4==0&&i%3!=0)
        lst[i]=lst[i]*lst[i]*lst[i];
    }
    for (i=0;i<lst.size();i++)
    sum+=lst[i];
    return sum;
}



