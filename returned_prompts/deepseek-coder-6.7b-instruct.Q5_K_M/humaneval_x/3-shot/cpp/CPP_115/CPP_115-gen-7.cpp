    int total=0;
    int i,j;
    for  (i=0;i<grid.size();i++)
        for  (j=0;j<grid[0].size();j++)
            total+=grid[i][j];

    return (total+capacity-1)/capacity;
}


