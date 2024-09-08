#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> minPath(vector<vector<int>> grid, int k){
    vector<int> path;
    int m = grid.size();
    vector<vector<int>> dp(m,vector<int>(m,k+1));
    for(int i = 0; i < m; i++){
        for(int j = 0; j < m; j++){
            dp[i][j] = min(dp[i][j],grid[i][j]);
        }
    }
    int dx[4] = {-1,1,0,0}, dy[4] = {0,0,-1,1};
    queue<pair<int,int>> q;
    q.push({0,0});
    dp[0][0] = k;
    while(!q.empty()){
        auto [x,y] = q.front();
        q.pop();
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i], ny = y + dy[i];
            if(nx < 0 || ny < 0 || nx >= m || ny >= m) continue;
            if(dp[nx][ny] > dp[x][y] - 1){
                dp[nx][ny] = dp[x][y] - 1;
                q.push({nx,ny});
            }
        }
    }
    int x = m - 1, y = m - 1;
    while(x != 0 || y != 0){
        path.push_back(grid[x][y]);
        int minn = 2*m;
        int px = x, py = y;
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i], ny = y + dy[i];
            if(nx < 0 || ny < 0 || nx >= m || ny >= m || dp[nx][ny] == k+1) continue;
            if(dp[nx][ny] < minn){
                minn = dp[nx][ny];
                px = nx, py = ny;
            }
        }
        x = px, y = py;
    }
    path.push_back(grid[0][0]);
    reverse(path.begin(),path.end());
    return path;
}
int main(){
    vector<vector<int>> grid = {{5,9,3},{4,1,6},{7,8,2}};
    int k = 1;
    vector<int>