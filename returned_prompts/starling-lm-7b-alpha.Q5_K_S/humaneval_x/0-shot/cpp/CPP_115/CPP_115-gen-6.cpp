    if(grid.empty()) return 0;
    int n = grid.size(),m = grid[0].size();
    int ans = 0,sum = 0;
    for(int i = 0;i < n;i++){
        for(int j = 0;j < m;j++)
            if(grid[i][j]) sum++;
    }
    if(sum % capacity == 0) return sum / capacity;
    return max_fill(grid,capacity)+1;
}

int main(){
    vector<vector<int>> grid = {{0,0,1,0},{0,1,0,0},{1,1,1,1}};
    int capacity = 1;
    printf("%d\n",max_fill(grid,capacity));
    return 0;
}




*/


#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<vector<int>> grid = {{0,0,1,0},{0,1,0,0},{1,1,1,1}};
    int capacity = 1;
    cout << max_fill(grid,capacity) << endl;
    return 0;
}

```