    int rows = grid.size(), cols = grid[0].size(), water = 0, max_water = 0;
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            if (grid[i][j] == 1)
                water++;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 1) {
                int filled_buckets = (water + capacity - 1) / capacity;
                int empty_buckets = filled_buckets - 1;
                int extra_water = empty_buckets * capacity - water;
                if (extra_water > max_water)
                    max_water = extra_water;
            }
        }
    }
    return max_water;
}
int main() {
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity = 1;
    printf("%d\n", max_fill(grid, capacity));
    return 0;
}

*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int max_fill(vector<vector<int>> grid, int capacity) {
    int rows = grid.size(), cols = grid[0].size(), water = 0, max_water = 0;
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            if (grid[i][j] == 1)
                water++;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 1) {
                int filled_buckets = (water + capacity - 1) / capacity;
                int empty_buckets = filled_buckets - 1;
               