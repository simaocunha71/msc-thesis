    long long sum=0;
    float diff;
    int i;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]>0 && lst[i]==lst[i])
        {
            diff=lst[i];
            sum+=diff*diff;
        }
    }
    return sum;
}



