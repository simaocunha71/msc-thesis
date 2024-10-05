    int count=0;
    int i,j;
    int a,b;
    for (i=1;i<pow(10,n-1);i++)
    {
        a=i%10;
        b=i/10;
        if (a==1 || b==1)
        count++;
    }
    return count;
}

