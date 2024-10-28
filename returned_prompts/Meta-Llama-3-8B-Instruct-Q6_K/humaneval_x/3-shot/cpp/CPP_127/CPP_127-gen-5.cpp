    int start=max(interval1[0],interval2[0]);
    int end=min(interval1[1],interval2[1]);
    
    if (start>end)
        return "NO";
    
    int length=end-start;
    
    if (length==1)
        return "NO";
    
    bool is_prime=true;
    for (int i=2;i<=sqrt(length);i++)
    {
        if (length%i==0)
        {
            is_prime=false;
            break;
        }
    }
    if (is_prime)
        return "YES";
    else
        return "NO";
}