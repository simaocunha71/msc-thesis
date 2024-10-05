    int rows = grid.size();
    int cols = grid[0].size();
    int total_water = 0;
    int total_buckets = 0;

    // Calculate total amount of water in all wells
    for(int i=0; i<rows; i++)
        for(int j=0; j<cols; j++)
            total_water += grid[i][j];

    // Calculate total number of buckets needed to fill all wells
    total_buckets = total_water / capacity;
    if(total_water % capacity != 0) total_buckets++;

    return total_buckets;
}

int main(){
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int bucket_capacity = 1;
    printf("%d\n", max_fill(grid, bucket_capacity)); // Output: 6

    grid = {{0,0,1,1}, {0,0,0,0}, {1,1,1,1}, {0,1,1,1}};
    bucket_capacity = 2;
    printf("%d\n", max_fill(grid, bucket_capacity)); // Output: 5

    grid = {{0,0,0}, {0,0,0}};
    bucket_capacity = 5;
    printf("%d\n", max_fill(grid, bucket_capacity)); // Output: 0

    return 0;
}
*/

#include<iostream>
#include<vector>
using namespace std;

int max_fill(vector<vector<int>> grid,int capacity){
    int rows = grid.size();
    int cols = grid[0].size();
    int total_water = 0;
    int total_buckets = 0;

    // Calculate total amount of water in all wells
    for(int i=0; i<rows; i++)
        for(int j=0; j<cols; j++)
            total_water += grid[