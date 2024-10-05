    int i,j;
    vector<int> primes;
    for (i=0;i<lst.size();i++)
    for (j=0;j<primes.size();j++)
    if (lst[i]%primes[j]==0)
    lst[i]/=primes[j];

    return lst[0];
}



