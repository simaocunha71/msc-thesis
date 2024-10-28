    for (int i=int(sqrt(float(n)))+1;i>1;i--)
    if (n%i==0)
    return largest_prime_factor(n/i);

    return n;
}


