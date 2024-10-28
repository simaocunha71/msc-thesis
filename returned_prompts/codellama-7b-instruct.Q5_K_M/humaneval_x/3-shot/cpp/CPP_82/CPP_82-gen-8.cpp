    int i;
    bool is_prime=true;
    if (str.length()==0)
    return false;
    if (str.length()==1)
    return true;
    for (i=2;i<=str.length();i++)
    if (str.length()%i==0)
    is_prime=false;
    return is_prime;
}

