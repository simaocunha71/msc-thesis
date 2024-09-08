    int res = 0, filled = 0;
    for(int i = 0; i < grid.size(); i++){
        for(int j = 0; j < grid[i].size(); j++){
            if(grid[i][j] == 1){
                filled++;
            }
        }
    }
    int bucket = filled / capacity;
    filled %= capacity;
    res += bucket;
    while(filled > 0){
        res++;
        filled -= capacity;
    }
    return res;
}

int main(){
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity = 1;
    printf("%d\n",max_fill(grid, capacity));  
    return 0;
}
/* The solution calculates the total water to be extracted from the grid.
It first calculates the total amount of water in the grid and divides it by the bucket capacity.
This gives the number of full buckets needed. The remaining water is then calculated by taking the modulus of the total water with the bucket capacity.
Then the program enters a loop where it fills the remaining water in the buckets, incrementing the result each time until the remaining water is 0.
The result is the total number of times the buckets need to be lowered. */
```
Solution:
```c
#include <stdio.h>
#include <vector>
using namespace std;

int max_fill(vector<vector<int>>& grid, int capacity) {
    int res = 0, filled = 0;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[i].size(); j++) {
            if (grid[i][j] == 1) {
                filled++;
            }
        }
    }
    int bucket = filled / capacity;
    filled %= capacity;
    res += bucket;
    while (filled > 0) {
        res++;
        filled -= capacity;
    }
    return res;
}

int main() {
    vector<vector<int>> grid = {{0, 0, 1, 0}, {0, 1, 0, 0}, {1, 1, 1, 1}};
    int capacity = 1;
    printf("%d\n", max_fill(grid, capacity));  
    return 0;
}
```
Explanation:

The program calculates the total amount of water in the grid by iterating over each