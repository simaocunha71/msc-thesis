    vector<int> tri;
    if (n==0)
    {
        tri.push_back(1);
        tri.push_back(3);
        tri.push_back(2);
        tri.push_back(8);
        return tri;
    }
    int i;
    for (i=0;i<n+1;i++)
    {
        tri.push_back(1+i/2);
        if (i%2==1)
        {
            int j;
            int sum=0;
            for (j=0;j<i+1;j++)
            sum+=tri[j];
            tri[i]=sum;
        }
    }
    return tri;
}

