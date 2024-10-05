    int sum=0;
    for(int i=1;i<=n;i++)
    {
        sum+=i;
    }
    return sum;
}  // This solution is not efficient for large values of n, as it uses a loop. A more efficient solution would be to use the formula for the sum of an arithmetic series: sum_to_n(n) = n*(n+1)/2


