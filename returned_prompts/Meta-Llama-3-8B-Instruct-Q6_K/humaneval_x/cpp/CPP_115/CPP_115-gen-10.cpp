    int ans = 0;
    int m = grid.size();
    int n = grid[0].size();
    for(int i = 0; i < m; i++){
        int j = 0;
        while(j < n && grid[i][j] == 0) j++;
        int start = j;
        int end = n;
        while(j < end){
            if(grid[i][j] == 1) j++;
            else if(grid[i][j] == 0) break;
        }
        int w = j - start;
        ans += (w + capacity - 1)/capacity;
    }
    return ans;
}
int main(){
    vector<vector<int>> grid = {{0,0,1,0},{0,1,0,0},{1,1,1,1}};
    int capacity = 1;
    printf("%d\n",max_fill(grid, capacity));
    return 0;
}

B:
    int max_fill(vector<vector<int>> grid, int capacity) {
        int n = grid.size();
        int m = grid[0].size();
        int res = 0;
        for(int i = 0; i < n; i++) {
            int j = 0, w = 0;
            while(j < m) {
                if(grid[i][j] == 1) {
                    w++;
                    j++;
                } else j++;
            }
            res += (w + capacity - 1) / capacity;
        }
        return res;
    }
    int main() {
        vector<vector<int>> grid = {{0,0,1,0},{0,1,0,0},{1,1,1,1}};
        int capacity = 1;
        cout << max_fill(grid, capacity) << endl;
        return 0;
    }

C:
    int max_fill(vector<vector<int>> grid, int capacity) {
        int n = grid.size();
        int m = grid[0].size();
        int res = 0;
        for(int i = 0; i < n; i++) {
            int w = 0;
            for(int j = 0; j < m; j++) {
                if(grid[i][j] == 1) w++;
                else break;
            }
            res += (w + capacity - 1) / capacity;
        }
        return res;
    }
    int main() {
        vector<vector<int>> grid = {{