    if (a==1) return false;
    for (int i=2;i<100;i++)
    if (a%i==0)
    if (is_prime(i))
    if (is_prime(a/i))
    return true;
    return false;
}




