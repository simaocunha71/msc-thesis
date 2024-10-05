    string result;
    int sum=0,i,rem;
    while (N!=0)
    {
        rem=N%2;
        sum+=rem;
        N/=2;
    }
    while (sum!=0)
    {
        result+=(char)('0'+sum%2);
        sum/=2;
    }
    return result;
}


