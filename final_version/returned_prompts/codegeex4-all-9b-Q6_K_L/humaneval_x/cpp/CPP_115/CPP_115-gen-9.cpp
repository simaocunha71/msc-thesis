/*
You are given a rectangular grid of wells. Each row represents a single well,
and each 1 in a row represents a single unit of water.
Each well has a corresponding bucket that can be used to extract water from it, 
and all buckets have the same capacity.
Your task is to use the buckets to empty the wells.
Output the number of times you need to lower the buckets.

Example 1:
    Input: 
        grid : {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}}
        bucket_capacity : 1
    Output: 6

Example 2:
    Input: 
        grid : {{0,0,1,1}, {0,0,0,0}, {1,1,1,1}, {0,1,1,1}}
        bucket_capacity : 2
    Output: 5

Example 3:
    Input: 
        grid : {{0,0,0}, {0,0,0}}
        bucket_capacity : 5
    Output: 0

Constraints:
    * all wells have the same length
    * 1 <= grid.length <= 10^2
    * 1 <= grid{:,1}.length <= 10^2
    * grid{i}{j} -> 0 | 1
    * 1 <= capacity <= 10
*/
#include<stdio.h>
#include<vector>
using namespace std;
int max_fill(vector<vector<int>> grid,int capacity){
    int total_rows = grid.size();
    int total_cols = grid[0].size();
    int total_buckets = 0;
    for(int i=0;i<total_rows;i++){
        int current_row = 0;
        for(int j=0;j<total_cols;j++){
            current_row += grid[i][j];
        }
        int no_buckets = current_row / capacity;
        int remainder = current_row % capacity;
        if(remainder != 0){
            no_buckets++;
        }
        total_buckets += no_buckets;
    }
    return total_buckets;
}

void test_max_fill(){

    vector<vector<int>> grid1 = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity1 = 1;
    int result1 = max_fill(grid1,capacity1);
    printf("Test 1 - Result: %d\n",result1