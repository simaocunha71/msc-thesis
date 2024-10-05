    int i,j;
    int min=grid[0][0];
    int min_pos=1;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[0].size();j++)
    if (grid[i][j]<min){
        min=grid[i][j];
        min_pos=(i+1)*10+(j+1);
    }
    vector<int> min_path;
    int pos=min_pos;
    int pos_i=(pos-1)/10;
    int pos_j=(pos-1)%10;
    min_path.push_back(grid[pos_i][pos_j]);
    for (i=0;i<k;i++){
        if (i%2==0){
            if (pos_i>1)
                pos_i-=1;
        }
        else{
            if (pos_i<grid.size()-1)
                pos_i+=1;
        }
        min_path.push_back(grid[pos_i][pos_j]);
    }
    return min_path;
}

