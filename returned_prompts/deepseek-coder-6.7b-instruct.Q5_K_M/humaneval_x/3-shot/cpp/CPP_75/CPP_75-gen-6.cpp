    int prime_factors_count = 0;
    for(int i = 2; a > 1; i++)
    {
        while(a % i == 0)
        {
            prime_factors_count++;
            a /= i;
        }
    }
    return prime_factors_count == 3;
}

