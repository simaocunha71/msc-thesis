    int i,j,fill,sum,total_fill;
    fill=0;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    {
        sum=0;
        for (int k=j;k<grid[i].size();k++)
        {
            sum+=grid[i][k];
            if (sum==capacity)
            {
                fill+=1;
                sum=0;
                j=k+1;
            }
            if (sum>capacity)
            {
                j=k;
                break;
            }
        }
    }
    return fill;
}



