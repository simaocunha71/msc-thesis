    int n = grid.size();
    vector<int> dp(n*n);
    int i = 0;
    for (auto &v : dp){
        v = i++;
    }
    //dp[i][j] is the minimum distance from (0,0) to (i,j)
    int m = n*n;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            dp[i*n+j] = min(dp[(i-1)*n+j], dp[i*n+(j-1)]) + grid[i][j];
        }
    }
    vector<int> res;
    int cur = m;
    while (k--){
        int i = cur / n;
        int j = cur % n;
        res.push_back(grid[i][j]);
        cur = dp[cur];
    }
    return res;
}
int main(){
    int n;
    scanf("%d", &n);
    vector<vector<int>> grid(n, vector<int>(n));
    for (auto &v : grid){
        for (auto &i : v){
            scanf("%d", &i);
        }
    }
    int k;
    scanf("%d", &k);
    vector<int> res = minPath(grid, k);
    for (auto i : res){
        printf("%d ", i);
    }
    return 0;
}
