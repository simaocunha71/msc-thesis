    int len=str.length();
    bool is_prime=true;
    if(len<2)
        return is_prime;
    for(int i=2;i<=sqrt(len);i++)
    {
        if(len%i==0)
        {
            is_prime=false;
            break;
        }
    }
    return is_prime;
}