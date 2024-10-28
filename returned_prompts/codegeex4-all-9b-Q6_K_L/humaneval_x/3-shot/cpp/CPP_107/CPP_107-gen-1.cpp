    vector<int> even_odd(2,0);
    int i;
    for (i=1;i<=n;i++)
    if (i%2==0)
    {
        int temp=i;
        int reverse=0;
        while (temp!=0)
        {
            reverse*=10;
            reverse+=temp%10;
            temp/=10;
        }
        if (reverse==i)
        even_odd[0]+=1;
    }
    else
    {
        int temp=i;
        int reverse=0;
        while (temp!=0)
        {
            reverse*=10;
            reverse+=temp%10;
            temp/=10;
        }
        if (reverse==i)
        even_odd[1]+=1;
    }
    return even_odd;
}

