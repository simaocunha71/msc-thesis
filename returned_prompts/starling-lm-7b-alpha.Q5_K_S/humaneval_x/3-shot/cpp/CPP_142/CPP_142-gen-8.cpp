    int i;
    int sum=0;
    for (i=0;i<lst.size();i++)
    {
        if (i%3==0)
        {
            sum+=lst[i]*lst[i];
        }
        if (i%4==0 && i%3!=0)
        {
            sum+=lst[i]*lst[i]*lst[i];
        }
    }
    return sum;
}



