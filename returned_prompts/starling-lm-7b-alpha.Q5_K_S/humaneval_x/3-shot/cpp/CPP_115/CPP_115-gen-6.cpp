    int n=grid.size();
    int m=grid[0].size();
    int i,j,k;
    int bucket_left;
    int result=0;
    while (true)
    {
        bucket_left=capacity;
        for (i=0;i<n;i++)
        for (j=0;j<m;j++)
        if (grid[i][j]>0)
        {
            bucket_left-=grid[i][j];
            grid[i][j]=0;
        }
        if (bucket_left==0)
        {
        result+=1;
        if (i>=n-1 and j>=m-1)
        break;
        }
    }
    return result;
}




