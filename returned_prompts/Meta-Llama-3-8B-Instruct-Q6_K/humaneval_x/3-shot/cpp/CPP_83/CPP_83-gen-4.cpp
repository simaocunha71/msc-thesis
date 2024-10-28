    int count=0;
    if(n==1)
    {
        count+=2; // 1 and 10
    }
    else
    {
        count+=2; // 10^n and 1*10^(n-1)
        count+=9*pow(10,n-1); // all numbers ending with 1
    }
    return count;
} 
