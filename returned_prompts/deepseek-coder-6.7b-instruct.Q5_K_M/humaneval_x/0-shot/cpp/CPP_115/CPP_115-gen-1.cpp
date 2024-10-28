    int total_wells=0;
    int total_water=0;
    for (int i = 0; i < grid.size(); i++)
    {
        for (int j = 0; j < grid[i].size(); j++)
        {
            if(grid[i][j] == 1){
                total_wells++;
                total_water++;
            }
        }
        
    }
    if(total_water<=capacity){
        return total_wells;
    }
    else{
        return total_wells+(total_water/capacity);
    }
    
}

int main() {
    vector<vector<int>> grid = {{0,0,1,1},{0,0,0,0},{1,1,1,1},{0,1,1,1}};
    int capacity = 2;
    int result = max_fill(grid,capacity);
    printf("%d",result);
    return 0;
}

*/

#include <stdio.h>
#include <vector>
using namespace std;

int max_fill(vector<vector<int>> grid, int capacity) {
    int total_wells = 0;
    int total_water = 0;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[i].size(); j++) {
            if (grid[i][j] == 1) {
                total_wells++;
                total_water++;
            }
        }
    }
    if (total_water <= capacity) {
        return total_wells;
    } else {
        return total_wells + (total_water / capacity);
    }
}

int main() {
    vector<vector<int>> grid = {{0,0,1,1},{0,0,0,0},{1,1,1,1},{0,1,1,1}};
    int capacity = 2;
    int result = max_fill(grid, capacity);
    printf("%d", result);
    return 0;