    int sum=0;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]>1)
        {
            if (lst[i]%2==0)
            {
                while (lst[i]%2==0)
                lst[i]/=2;
            }
            if (lst[i]%3==0)
            {
                while (lst[i]%3==0)
                lst[i]/=3;
            }
        }
    }
    for (int i=0;i<lst.size();i++)
    sum+=lst[i];
    return sum;
}


