    /*
    Create a new 2D array of the same size as the input grid.
    Initialize the new array to zeros.
    */
    int rows = grid.size();
    int cols = grid[0].size();
    vector<vector<int>> bucket(rows,vector<int>(cols,0));
    int total = 0;

B:
    /*
    Iterate through the grid.
    If the cell is one (i.e., a well), add the capacity to the bucket's corresponding cell.
    */
    for(int i=0; i<rows; i++){
        for(int j=0; j<cols; j++){
            if(grid[i][j] == 1){
                bucket[i][j] = capacity;
                total += capacity;
            }
        }
    }

C:
    /*
    The number of times you need to lower the buckets is the total amount of water in the wells.
    */
    return total;
}
int main(){
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity = 1;
    int times = max_fill(grid,capacity);
    printf("Number of times you need to lower the buckets: %d",times);
    return 0;
}

*/

#include <bits/stdc++.h>
using namespace std;

int max_fill(vector<vector<int>> grid, int capacity) {
    int rows = grid.size();
    int cols = grid[0].size();
    vector<vector<int>> bucket(rows, vector<int>(cols, 0));
    int total = 0;

    for(int i=0; i<rows; i++){
        for(int j=0; j<cols; j++){
            if(grid[i][j] == 1){
                bucket[i][j] = capacity;
                total += capacity;
            }
        }
    }

    return total;
}

int main() {
   