    int i;
    int total=0;
    int size=lst.size();
    for (i=0;i<size;i++)
    {
        if (i%3==0)
        {
        total+=lst[i]*lst[i];
        }
        if (i%4==0 && i%3!=0)
        {
        total+=lst[i]*lst[i]*lst[i];
        }
    }
    return total;
}


