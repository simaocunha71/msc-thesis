    vector<int> factors;
    int factor=2;
    while (n>1)
    {
        if (n%factor==0){
            factors.push_back(factor);
            n=n/factor;
        }
        else{
            factor+=1;
        }
    }
    return factors;
}

