
C:
```c
#include <stdio.h>
#include <vector>

using namespace std;

int bucket_fill(vector<vector<int>>& grid, int capacity) {
    int n = grid.size();
    int res = 0;
    while (true) {
        int fill = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < grid