    int count = 0;
    for(int i=0;i<grid.size();i++){
        for(int j=0;j<grid[i].size();j++){
            if(grid[i][j] == 1){
                count++;
            }
        }
    }
    return count/capacity;
B:
    return (grid.size()*grid[0].size()+capacity-1)/capacity;
}

// Test cases:
// max_fill({{0,0,1,0},{0,1,0,0},{1,1,1,1}},1) => 6
// max_fill({{0,0,1,1},{0,0,0,0},{1,1,1,1},{0,1,1,1}},2) => 5
// max_fill({{0,0,0},{0,0,0}},5) => 0

int main(){
    // Test cases
    printf("%d\n",max_fill({{0,0,1,0},{0,1,0,0},{1,1,1,1}},1)); // Output: 6
    printf("%d\n",max_fill({{0,0,1,1},{0,0,0,0},{1,1,1,1},{0,1,1,1}},2)); // Output: 5
    printf("%d\n",max_fill({{0,0,0},{0,0,0}},5)); // Output: 0
    return 0;
}

// Explanation:
// In the first test case, the total number of wells is 9 and the bucket capacity is 1. So, 9/1 = 9 times you need to lower the buckets.
// In the second test case, the total number of wells is 12 and the bucket capacity is 2. So, 12/2 = 6 times you need to lower the buckets.
// In the third test case, the total number of wells is 6 and the bucket capacity is 5. So, 6/5 = 1 times you need to lower the buckets.

// S