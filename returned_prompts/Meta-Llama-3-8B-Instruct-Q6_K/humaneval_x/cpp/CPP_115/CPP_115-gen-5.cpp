    int sum =0;
    for(int i =0; i < grid.size(); i++){
        sum += grid[i].size();
    }
    int count =0;
    for(int i =0; i < grid.size(); i++){
        for(int j =0; j < grid[i].size(); j++){
            if(grid[i][j] == 1){
                count++;
            }
        }
    }
    return count;
}
int min_buckets(vector<vector<int>> grid,int capacity){
    int sum =0;
    for(int i =0; i < grid.size(); i++){
        sum += grid[i].size();
    }
    int count =0;
    while(sum > 0){
        int fill =0;
        for(int i =0; i < grid.size(); i++){
            for(int j =0; j < grid[i].size(); j++){
                if(grid[i][j] == 1){
                    fill++;
                    grid[i][j] =0;
                }
            }
        }
        if(fill == 0) break;
        sum -= fill;
        count++;
        if(fill <= capacity){
            fill = capacity;
        }
    }
    return count;
}
int main(){
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity = 1;
    printf("%d",min_buckets(grid, capacity));
    return 0;
}*/



C:
```c
#include <stdio.h>
#include <vector>
using namespace std;

int max_fill(vector<vector<int>> grid, int capacity) {
    int sum = 0;
    for (int i = 0; i < grid.size(); i++) {
        sum += grid[i].size();
    }
    int count = 0;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[i].size(); j++) {
            if (grid[i][j] == 1) {
                count++;
            }
        }
    }
    return count;
}

int min_buckets(vector<vector<int>> grid, int capacity) {
    int sum = 0;
    for (int i = 0; i < grid.size(); i++) {
        sum += grid[i].size();
    }
    int count = 0;
    while (sum > 0) {
        int fill =