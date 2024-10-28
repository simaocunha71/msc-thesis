    int collisions=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(i!=j)
            {
                int distance=abs(i-j);
                if(distance%2==0)
                collisions++;
            }
        }
    }
    return collisions;
}

