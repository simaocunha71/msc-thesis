    int i,j;
    int sum=0;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    if (grid[i][j]==1){
        sum+=1;
        if (sum%capacity==0)
        sum=0;
    }
    return sum;
}

