    vector<int> factors;
    int i;
    for(i=2;i<=n;i++)
    {
        int count=0;
        while(n%i==0)
        {
            count++;
            n=n/i;
        }
        if(count>0)
        {
            factors.push_back(i);
            for(int j=0;j<count;j++)
            {
                factors.push_back(i);
            }
        }
    }
    return factors;
}  // This function will return the prime factors of a number in the form of a vector


