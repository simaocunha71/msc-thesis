    int i,j;
    int index=0;
    int index_i=0;
    int index_j=0;
    int counter=0;
    vector<int> result;
    vector<int> min_result;
    int min_counter;
    int min_index;
    int min_index_i;
    int min_index_j;
    int min_index_i_counter;
    int min_index_j_counter;
    vector<int> min_result_counter;
    vector<vector<int>> min_grid;
    while (counter<k){
        result.push_back(grid[index_i][index_j]);
        if (index_i>0&&index_j<(grid[0].size()-1)){
            if (counter+1<k&&grid[index_i-1][index_j]>grid[index_i][index_j+1]){
                index_i-=1;
                index_j+=1;
            }
            else{
                index_i+=1;
                index_j-=1;
            }
        }
        if (index_i<(grid.size()-1)&&index_j<(grid[0].size()-1)){
            if (counter+1<k&&grid[index_i][index_j+1]>grid[index_i+1][index_j]){
                index_i+=1;
                index_j+=1;
            }
            else{
                index_i+=1;
                index_j-=1;
            }
        }
        if (index_i<(grid.size()-1)&&index_j>0){
            if (counter+1<k&&grid[index_i][index_j-1]>grid[index_i+1][index_j]){
                index_i+=1;
                index_j-=1;
            }
            else{
                index_i+=1;
                index_j+=1;
            }
        }
        if (index_i>0&&index_j>0