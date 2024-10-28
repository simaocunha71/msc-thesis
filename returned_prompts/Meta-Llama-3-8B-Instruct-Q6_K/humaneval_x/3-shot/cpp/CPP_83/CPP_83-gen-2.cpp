    int count=0;
    int i;
    for (i=10^(n-1);i<10^n;i++)
    {
        if ((i%10==1)||(i/10^((n-1))%10==1))
        count++;
    }
    return count;
}  // This solution is not correct as it only checks if the number ends with 1
// It does not consider the case when the number starts with 1
// A correct solution would be to check both conditions


