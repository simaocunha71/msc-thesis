    vector<int> factors;
    int i=2;
    while (i*i<=n)
    {
        if (n%i==0){
            int count=0;
            while (n%i==0){
                count+=1;
                n=n/i;
            }
            factors.push_back(i);
            i=2;
            continue;
        }
        i+=1;
    }
    if (n>1)
    factors.push_back(n);
    return factors;
}


