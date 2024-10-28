    int i,sum;
    float x;
    sum=0;
    for (i=0;i<lst.size();i++)
    {
        x=ceil(lst[i]);
        sum+=x*x;
    }
    return sum;
}


