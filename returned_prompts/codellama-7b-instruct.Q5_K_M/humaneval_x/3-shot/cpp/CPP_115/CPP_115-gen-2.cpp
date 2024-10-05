    int min_fill=0;
    int i,j;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[0].size();j++)
    if (grid[i][j]==1)
    min_fill+=1;
    return min(min_fill,capacity);
}


int main(){
    int m,n;
    printf("Enter the size of the grid: ");
    scanf("%d %d",&m,&n);
    vector<vector<int>> grid;
    printf("Enter the values of the grid: \n");
    for (int i=0;i<m;i++){
        vector<int> row;
        for (int j=0;j<n;j++)
        row.push_back(0);
        grid.push_back(row);
    }
    printf("Enter the values of the grid: \n");
    for (int i=0;i<m;i++){
        for (int j=0;j<n;j++)
        scanf("%d",&grid[i][j]);
    }
    int capacity;
    printf("Enter the capacity of the bucket: ");
    scanf("%d",&capacity);
    int max_fill=max_fill(grid,capacity);
    int min_fill=min_fill(grid,capacity);
    printf("The maximum fill is %d\n",max_fill);
    printf("The minimum fill is %d\n",min_fill);
    return 0;
}
































