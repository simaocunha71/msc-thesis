    int count=0;
    int i;
    for (i=1;i<10;i++)
    {
        if (i==1 || i==10)
        count+=pow(10,n-1);
    }
    return count;
}


