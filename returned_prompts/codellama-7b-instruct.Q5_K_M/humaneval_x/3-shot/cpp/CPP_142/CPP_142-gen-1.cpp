    int sum=0;
    int i;
    for (i=0;i<lst.size();i++)
    {
        if ((i%3==0)&&(i%4!=0))
        sum+=lst[i]*lst[i];
        if ((i%4==0)&&(i%3!=0))
        sum+=pow(lst[i],3);
    }
    return sum;
}


