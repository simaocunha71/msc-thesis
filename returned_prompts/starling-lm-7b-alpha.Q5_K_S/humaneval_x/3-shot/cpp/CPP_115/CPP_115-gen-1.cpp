    int i,j;
    int n=grid.size();
    int m=grid[0].size();
    int total_fill=0;

    while (true)
    {
        int done=true;
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                if (grid[i][j]>0){
                    grid[i][j]-=1;
                    total_fill+=1;
                    done=false;
                    break;
                }
            }
            if (!done)
            break;
        }
        if (done)
        return total_fill;
    }
}



