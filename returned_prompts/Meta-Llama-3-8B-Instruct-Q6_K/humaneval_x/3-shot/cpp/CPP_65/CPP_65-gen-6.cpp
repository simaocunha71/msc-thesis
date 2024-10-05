    int n=0;
    int digit;
    string s;
    while(x>0)
    {
        digit=x%10;
        x=x/10;
        n++;
    }
    if(shift>=n)
        shift%=n;
    for(int i=n-1;i>=0;i--)
    {
        if(i<shift)
            s+=to_string(digit);
        else
            s+=to_string((x%10));
        x=x/10;
    }
    return s;
}  // This function doesn't check whether the input integer is positive or not. It's not a good practice in programming. It should be handled by the function.  



