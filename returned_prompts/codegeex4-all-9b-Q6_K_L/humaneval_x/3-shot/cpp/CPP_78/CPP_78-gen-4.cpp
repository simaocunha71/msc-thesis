    int count=0;
    vector<int> primes={2,3,5,7,11,13,17,19};
    string digits="0123456789ABCDEF";
    for (int i=0;i<digits.length();i++)
    if (num.find(digits[i])!=string::npos)
    if (find(primes.begin(),primes.end(),i)!=primes.end())
    count+=1;
    return count;
}

