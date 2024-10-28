    string res="";
    vector<bool> primes(101,true);
    vector<int> primes_index;
    int i,j;
    primes[0]=primes[1]=false;
    for (i=2;i<101;i++)
    if (primes[i])
    {
        res+=" ";
        for (j=i;j<sentence.length();j++)
        if (sentence[j]!=' ')
        {
            res+=sentence[j];
        }
        primes_index.push_back(i);
        for (j=i*i;j<101;j++)
        {
            primes[j]=false;
        }
    }
    return res;
}


