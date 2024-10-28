    int num_primes=0;
    int len=num.length();
    int i;
    for (i=0;i<len;i++)
    {
        if (num[i]>='A' && num[i]<='F')
        {
        string str=num[i];
        if (hex_key(str)==1)
        {
            if (str=="A")
            num_primes+=1;
            if (str=="B")
            num_primes+=1;
            if (str=="D")
            num_primes+=1;
            if (str=="E")
            num_primes+=1;
        }
        }
    }
    return num_primes;
}


