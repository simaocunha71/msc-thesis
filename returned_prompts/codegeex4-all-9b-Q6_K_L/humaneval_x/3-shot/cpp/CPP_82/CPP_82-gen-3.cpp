    int i;
    int len=str.length();
    bool is_prime=true;
    for (i=2;i<len;i++)
    {
        if (len%i==0)
        is_prime=false;
    }
    return is_prime;
}

