    long long sum=0;
    for (float x:lst)
    {
        if (x>0 && modf(x,&x)==0)
        sum+=x*x;
    }
    return sum;
} // 1.0 is a float, not an integer. We must check if x is an integer by using modf. If the fractional part is 0, then x is an integer. 2.0 is a float too. The sum must be long long type because the maximum sum is very large.  



