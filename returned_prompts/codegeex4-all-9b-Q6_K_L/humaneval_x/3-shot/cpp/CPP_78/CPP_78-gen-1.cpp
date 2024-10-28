    string primes="2357BD";
    int count=0;
    for (int i=0;i<num.length();i++)
    if (count(primes.begin(),primes.end(),num[i])>0)
    count++;
    return count;
}

