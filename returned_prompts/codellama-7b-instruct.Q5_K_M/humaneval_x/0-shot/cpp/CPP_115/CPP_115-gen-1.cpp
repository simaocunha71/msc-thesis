    int rows = grid.size();
    int cols = grid[0].size();
    int max_height = grid[0][0];
    int max_width = grid[0][0];

    for(int i=1;i<rows;i++){
        if(grid[i][0]>max_height)
            max_height = grid[i][0];
        if(grid[0][i]>max_width)
            max_width = grid[0][i];
    }

    int max_fill = 0;
    int min_fill = max_height;
    if(max_width<max_height){
        min_fill = max_width;
        max_fill = max_height;
    }
    else{
        max_fill = max_width;
        min_fill = max_height;
    }
    int start = 0;
    int end = 0;
    int times = 0;
    while(start<rows && end<cols){
        if(grid[start][end]==0){
            start++;
        }
        else{
            int min_fill_start = start;
            int max_fill_start = start;
            int min_fill_end = end;
            int max_fill_end = end;
            for(int i=start;i<rows;i++){
                if(grid[i][end]==0){
                    min_fill_start = i;
                    break;
                }
            }
            for(int i=start;i>=0;i--){
                if(grid[i][end]==0){
                    max_fill_start = i;
                    break;
                }
            }
            for(int j=end;j<cols;j++){
                if(grid[start][j]==0){
                    min_fill_end = j;
                    break;
                }
            }
            for(int j=end;j>=0;j--){
                if(grid[start][j]==0){
                    max_fill_end = j;
                    break;
                }
            }

            if