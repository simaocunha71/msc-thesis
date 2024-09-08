    int N = grid.size();
    vector<int> res;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            for(int path_len = 0; path_len < k; path_len++){
                if(path_len == 0){
                    res.push_back(grid[i][j]);
                }
                else{
                    int x = i - 1 >= 0 ? i - 1 : i;
                    int y = j - 1 >= 0 ? j - 1 : j;
                    if(x < N && y < N && grid[x][y] != grid[i][j]){
                        res.push_back(grid[x][y]);
                    }
                    else{
                        res.push_back(grid[i][j]);
                    }
                }
            }
        }
    }
    sort(res.begin(), res.end());
    return res;
}
int main(){
    vector<vector<int>> grid = {{1,2,3}, {4,5,6}, {7,8,9}};
    int k = 3;
    vector<int> res = minPath(grid, k);
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    printf("\n");
    return 0;
}
C:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdbool.h>

#define N 3

int cmp(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}

int main() {
    int grid[N][N] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int k = 3;
    int n = N * N;
    int *path = (int *)malloc(n * sizeof(int));
    int i, j, x, y, len;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            for (len = 0; len < k; len++) {
                if (len == 0) {
                    path[len] = grid[i][j];
                } else {
                    x = i - 1 >= 0 ? i - 1 : i;
                    y = j - 1 >= 0 ? j - 1 : j