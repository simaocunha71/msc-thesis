    int i;
    int primes=0;
    for (i=0;i<num.length();i++)
    {
        if (num[i]=='0'||num[i]=='1'||num[i]=='2'||num[i]=='3'||num[i]=='4'||num[i]=='5'||num[i]=='6'||num[i]=='7'||num[i]=='8'||num[i]=='9')
        {
        if (num[i]=='2'||num[i]=='3'||num[i]=='5'||num[i]=='7')
        {
        primes+=1;
        }
        }
        if (num[i]=='A'||num[i]=='B'||num[i]=='C'||num[i]=='D'||num[i]=='E'||num[i]=='F')
        {
        if (num[i]=='B'||num[i]=='D')
        {
        primes+=1;
        }
        }
    }
    return primes;
}



