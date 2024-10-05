    vector<int> prime_factors;
    int current_factor=2;
    while (n>1)
    {
        while (n%current_factor==0)
        {
            n/=current_factor;
            prime_factors.push_back(current_factor);
        }
        current_factor++;
    }
    return prime_factors;
}


