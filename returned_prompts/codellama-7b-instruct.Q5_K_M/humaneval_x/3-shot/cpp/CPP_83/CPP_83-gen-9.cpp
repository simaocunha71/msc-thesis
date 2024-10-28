    int count=0;
    for (int i=1;i<10*n;i++)
    {
        if (i/10%10==1 || i%10==1)
        count+=1;
    }
    return count;
}


