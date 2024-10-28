    vector<int> prime_factors;
    int current_factor=2;
    while (n>1)
    {
        while (n%current_factor==0)
        {
            prime_factors.push_back(current_factor);
            n/=current_factor;
        }
        current_factor++;
    }
    return prime_factors;
}



