    int n = grid.size();
    vector<vector<int>> dp(n,vector<int>(n,0));

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            dp[i][j] = grid[i][j];
        }
    }

    while(k > 0){
        vector<vector<int>> new_dp(n,vector<int>(n,0));
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                vector<int> v;
                v.push_back(grid[i][j]);
                if(i + 1 < n){
                    v.push_back(dp[i+1][j]);
                }
                if(j + 1 < n){
                    v.push_back(dp[i][j+1]);
                }
                new_dp[i][j] = *min_element(v.begin(),v.end());
            }
        }
        grid = new_dp;
        k--;
    }
    vector<int> res;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            res.push_back(grid[i][j]);
        }
    }
    return res;
}

int main(void){
    vector<vector<int>> grid = {{1,2,3},{4,5,6},{7,8,9}};
    int k = 3;
    vector<int> res = minPath(grid,k);
    for(auto e:res){
        printf("%d ",e);
    }
    return 0;
}

*/







































































