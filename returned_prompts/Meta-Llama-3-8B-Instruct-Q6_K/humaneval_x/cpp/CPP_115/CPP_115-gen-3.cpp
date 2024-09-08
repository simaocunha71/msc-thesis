    int count = 0;
    for(int i=0;i<grid.size();i++){
        int water = 0;
        for(int j=0;j<grid[i].size();j++){
            if(grid[i][j] == 1){
                water++;
            }
        }
        while(water > 0){
            int fill = min(water,capacity);
            water -= fill;
            count++;
        }
    }
    return count;
}
int main(){
    // Example 1
    vector<vector<int>> grid1 = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity1 = 1;
    cout << max_fill(grid1,capacity1) << endl; // Output: 6

    // Example 2
    vector<vector<int>> grid2 = {{0,0,1,1}, {0,0,0,0}, {1,1,1,1}, {0,1,1,1}};
    int capacity2 = 2;
    cout << max_fill(grid2,capacity2) << endl; // Output: 5

    // Example 3
    vector<vector<int>> grid3 = {{0,0,0}, {0,0,0}};
    int capacity3 = 5;
    cout << max_fill(grid3,capacity3) << endl; // Output: 0
    return 0;
}
B:
    The provided function max_fill calculates the number of times the buckets need to be lowered to empty the wells.
    The function iterates over each well in the grid and calculates the amount of water in the well.
    It then enters a loop to fill the buckets with water from the well, and for each bucket, it increments the count of times the buckets need to be lowered.
    The loop continues until all water in the well has been extracted. 
    The function returns the total count of times the buckets need to be lowered.
C:
    This problem can be solved by iterating over each well in the grid and extracting the water in the well into buckets.
    The number of times the buckets need to be lowered is equal to the total amount of water extracted divided by the capacity of the buckets.
    The problem can be solved using a single loop that iterates over each well in the grid.
    The loop calculates the amount of water in the well and then enters a nested loop