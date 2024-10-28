    int n=grid.size();
    int max=0;
    int i,j;
    for (i=0;i<n;i++)
    for (j=0;j<n;j++)
    {
        if (grid[i][j]==1){
            max=max+1;
            int k;
            for (k=i+1;k<n;k++)
            if (grid[k][j]==1)
            max=max+1;

        }
    }

    return max;
}




