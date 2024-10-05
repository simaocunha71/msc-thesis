    int i;
    int sum;
    for (i=2;i<n;i+=2)
    {
        sum=n-i;
        for (int j=2;j<sum;j+=2)
        {
            if (sum-j==i){
            return true;
            }
        }
    }
    return false;
}



