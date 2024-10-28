    int i;
    int sum=0;
    for (i=0;i<lst.size();i++)
    {
        if (i%4==0 && i%3!=0)
        sum+=pow(lst[i],3);
        if (i%3==0)
        sum+=pow(lst[i],2);
    }
    return sum;
}


