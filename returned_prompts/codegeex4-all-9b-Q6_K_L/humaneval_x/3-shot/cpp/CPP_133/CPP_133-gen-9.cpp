    int sum=0;
    int i;
    for (i=0;i<lst.size();i++)
    {
        sum+=(int)ceil(lst[i])*(int)ceil(lst[i]);
    }
    return sum;
}

