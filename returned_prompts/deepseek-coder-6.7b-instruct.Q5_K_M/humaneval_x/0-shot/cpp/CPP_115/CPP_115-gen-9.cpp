    int rows = grid.size();
    if(rows == 0) return 0;
    int cols = grid[0].size();
    vector<int> bucket(rows,0);
    int total_water = 0;
    for(int j=0;j<cols;j++){
        for(int i=0;i<rows;i++){
            if(grid[i][j] == 1){
                bucket[i]++;
                total_water++;
            }
        }
        sort(bucket.begin(), bucket.end());
        int bucket_idx = rows - 1;
        while(total_water > 0){
            while(bucket_idx >= 0 && bucket[bucket_idx] >= capacity){
                total_water -= capacity;
                bucket_idx--;
            }
            if(bucket_idx < 0) return rows - (total_water+1)/capacity;
            int need = capacity - bucket[bucket_idx];
            if(total_water < need) return rows - (bucket_idx+1);
            total_water -= need;
            bucket[bucket_idx] += need;
            sort(bucket.begin(), bucket.begin()+bucket_idx+1);
        }
    }
    return rows;
}

int main() {
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    printf("%d\n",max_fill(grid,1));
    return 0;
}

/*
This solution is for the problem of watering the wells. It uses bucket to fill the wells.
In this solution, we first determine the number of rows and columns in the grid.
Then we create an array bucket to keep track of water in each well.
We calculate total_water as the total amount of water in the grid.
Then we iterate over each column in the grid.
For each column, we iterate over each row in the grid, if the cell in the grid is 1, we increment the corresponding bucket and total_water.
Then we sort the bucket.
We use a while