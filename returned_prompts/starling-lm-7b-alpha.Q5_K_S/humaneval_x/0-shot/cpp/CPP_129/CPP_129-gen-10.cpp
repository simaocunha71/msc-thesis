    vector<pair<int, pair<int, int>>> q;
    int n = grid.size();
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            q.push_back(make_pair(grid[i][j], make_pair(i, j)));
        }
    }
    sort(q.begin(), q.end());
    vector<int> ans;
    while(ans.size() < k){
        pair<int, pair<int, int>> a = q.back(); q.pop_back();
        if(a.second.first > 0 && a.second.second > 0 && ans.size() < k){
            ans.push_back(grid[a.second.first][a.second.second]);
            if(ans.size() == k) break;
        }
        if(a.second.first < n - 1 && a.second.second > 0 && ans.size() < k){
            ans.push_back(grid[a.second.first + 1][a.second.second]);
            if(ans.size() == k) break;
        }
        if(a.second.first > 0 && a.second.second < n - 1 && ans.size() < k){
            ans.push_back(grid[a.second.first][a.second.second + 1]);
            if(ans.size() == k) break;
        }
        if(a.second.first < n - 1 && a.second.second < n - 1 && ans.size() < k){
            ans.push_back(grid[a.second.first + 1][a.second.second + 1]);
            if(ans.size() == k) break;
        }
    }
    return ans;
}
int main(){
    vector<vector<int>> grid = {{1,2,3},{4,5,6},{7,8,9}};
    int k = 3;
    vector<int> ans = minPath(grid, k);
    for(auto a : ans) printf("%d ", a