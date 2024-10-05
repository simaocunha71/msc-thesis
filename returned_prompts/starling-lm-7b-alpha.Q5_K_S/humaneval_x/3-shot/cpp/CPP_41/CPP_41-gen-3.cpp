    int i;
    int collisions=0;
    for (i=0;i<n;i++)
    {
    int left=i;
    int right=n-i-1;
    if (left<right)
    {
    collisions+=right-left;
    }
    }
    return collisions;
}



