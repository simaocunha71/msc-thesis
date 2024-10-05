    int i,j;
    vector<bool> prime;
    prime.resize(101,true);
    prime[0]=false;
    prime[1]=false;
    for (i=2;i<101;i++)
    if (prime[i])
    {
        for (j=i*i;j<101;j+=i)
        prime[j]=false;
    }
    int mults=0;
    for (i=2;i<101;i++)
    if (prime[i])
    {
        while (a%i==0)
        {
        a=a/i;
        mults+=1;
        }

        if (mults==3)
        return true;
    }
    return false;
}



