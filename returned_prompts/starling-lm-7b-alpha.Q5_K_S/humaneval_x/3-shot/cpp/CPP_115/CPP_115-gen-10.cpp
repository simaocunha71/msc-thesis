    int i,j;
    int wells_left=grid.size();
    int wells_filled=0;
    int bucket_left=capacity;
    int bucket_filled=0;
    int grid_sum=0;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    grid_sum+=grid[i][j];
    while (wells_filled<wells_left&&bucket_filled<bucket_left){
        if (grid_sum>0){
            for (i=0;i<grid.size();i++)
            for (j=0;j<grid[i].size();j++)
            if (grid[i][j]==1){
                grid[i][j]=0;
                bucket_filled+=1;
                grid_sum-=1;
                if (bucket_filled==capacity){
                    wells_filled+=1;
                    bucket_filled=0;
                }
                if (grid_sum==0)
                break;
            }
        }
        else
        break;
    }
    return wells_filled;
}


