    for (int i=2;i<=n;i+=2)
    {
        int sum=0;
        for (int j=2;j<=n;j+=2)
        {
            if (sum+i==n)
                return true;
            sum+=j;
        }
    }
    return false;
} // This function does not work correctly for large numbers due to time complexity.



