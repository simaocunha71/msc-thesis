    int i;
    int count=0;
    string primes="2357BD";
    string::iterator it;
    for (i=0;i<num.length();i++)
    {
        it=find(primes.begin(),primes.end(),num[i]);
        if (it!=primes.end())
        count+=1;
    }
    return count;
}

