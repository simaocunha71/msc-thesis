    int collisions=0;
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<n;j++)
        {
            if (i!=j && i+j==n-1)
                collisions++;
        }
    }
    return collisions;
} // O(n^2) complexity


