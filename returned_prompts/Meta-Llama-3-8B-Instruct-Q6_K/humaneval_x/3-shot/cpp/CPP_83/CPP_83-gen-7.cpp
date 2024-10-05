    int count=0;
    int num;
    for (num=1;num<10;num++)
    {
        if (num==1 || (num>9 && num%10==1))
        count++;
    }
    if (n>1)
    {
        for (num=10;num<pow(10,n);num++)
        {
            if (num/pow(10,n-1)%10==1 || num%10==1)
            count++;
        }
    }
    return count;
}
