    vector<int> all_factors;
    int i,j;
    for (i=2;i<n;i++)
    if (n%i==0){
        all_factors.push_back(i);
        while (n%i==0) n/=i;
    }
    if (n>1) all_factors.push_back(n);
    return all_factors;
}


