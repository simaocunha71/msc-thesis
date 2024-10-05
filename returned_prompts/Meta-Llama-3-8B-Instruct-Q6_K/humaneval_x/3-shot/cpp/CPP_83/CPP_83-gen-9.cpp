    int count=0;
    int i;
    for (i=10^(n-1);i<10^n;i++)
    {
        int num=i;
        if (num>=10 && num%10==1)
        {
            count++;
        }
    }
    return count;
}  



