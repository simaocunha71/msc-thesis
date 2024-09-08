    int n = grid.size();
    int m = grid[0].size();
    int count = 0;
    for(int i=0;i<n;i++){
        int j = 0;
        while(j < m && grid[i][j] == 0) j++;
        if(j == m) continue;
        int fill = 0;
        while(j < m && fill < capacity){
            fill += grid[i][j++];
        }
        if(fill > 0){
            count += fill;
            j = 0;
            while(j < m && grid[i][j] == 0) j++;
            if(j == m) continue;
            while(j < m && fill > 0){
                grid[i][j] -= 1;
                if(fill > 0) fill--;
                j++;
            }
        }
    }
    return count;
}
int main() {
    vector<vector<int>> grid = {{0,0,1,0},{0,1,0,0},{1,1,1,1}};
    int capacity = 1;
    printf("%d\n",max_fill(grid, capacity));
    return 0;
}
```

This program defines a function `max_fill` that takes a 2D vector `grid` representing the wells and an integer `capacity` representing the capacity of the buckets. The function returns the minimum number of times the buckets need to be lowered to empty the wells.

The function iterates over each row in the grid. For each row, it finds the first non-zero element (representing the starting point of the well) and then fills the bucket until it is full or the end of the well is reached. If the bucket is not full, it subtracts the remaining water from the well and increments the count of bucket lowers.

The function returns the total count of bucket lowers.

In the main function, an example grid and capacity are provided, and the `max_fill` function is called with these inputs. The result is printed to the console.

This program assumes that the input grid is a rectangular grid of 0s and 1s, where 0s represent empty spaces and 1s represent water. The capacity of the buckets is given as an integer. The program returns the minimum number of times the buckets need to be lowered to empty the wells.