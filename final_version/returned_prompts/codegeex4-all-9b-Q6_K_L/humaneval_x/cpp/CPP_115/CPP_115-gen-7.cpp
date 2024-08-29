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
    int max=0;
    for(int i=0;i<grid.size();i++){
        int temp=0;
        for(int j=0;j<grid[i].size();j++){
            temp+=grid[i][j];
        }
        if(temp>max)
            max=temp;
    }
    return (max+capacity-1)/capacity;
}
int main(){
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int bucket_capacity = 1;
    printf("%d\n",max_fill(grid,bucket_capacity));
    return 0;
}