    int n=grid.size();
    int m=grid[0].size();
    int i,j;
    int cnt=0;
    while(true){
        bool flag=true;
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                if(grid[i][j])
                    flag=false;
        if(flag)
            return cnt;
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                if(grid[i][j])
                    grid[i][j]-=capacity;
        cnt++;
    }
}
int main(){
    int n,m,i,j;
    scanf("%d%d%d",&n,&m,&i);
    vector<vector<int>> grid(n,vector<int>(m));
    for(j=0;j<n;j++)
        for(i=0;i<m;i++)
            scanf("%d",&grid[j][i]);
    printf("%d\n",max_fill(grid,i));
    return 0;
}

*/
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxDistance(vector<vector<int>>& grid, int K) {
        int n = grid.size(), m = grid[0].size();
        queue<pair<int, int>> q;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 1) {
                    q.emplace(i, j);
                }
            }
        }
        int res = 0;
        while (!q.empty()) {
            int sz = q.size();
            while (sz--) {
                int x = q.front().first, y = q.front().second;
                q.pop();
                for (int dx = -1; dx <= 1; ++dx) {
