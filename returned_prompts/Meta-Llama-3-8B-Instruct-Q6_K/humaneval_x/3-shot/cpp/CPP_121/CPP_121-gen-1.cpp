    int sum=0;
    int i;
    for (i=0;i<lst.size();i++)
    {
        if (i%2==0 && lst[i]%2!=0)
        {
            sum+=lst[i];
        }
    }
    return sum;
}