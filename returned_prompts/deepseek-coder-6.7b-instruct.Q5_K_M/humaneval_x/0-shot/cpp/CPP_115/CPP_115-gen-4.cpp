    int n=grid.size(),m=grid[0].size();
    int ans=0;
    vector<int> arr(n,0);

B:
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(grid[i][j]==1){
                grid[i][j]=0;
                int idx=-1;
                for(int k=0;k<n;k++){
                    if(arr[k]<m && (idx==-1 || grid[k][arr[k]]>grid[i][j])){
                        idx=k;
                    }
                }
                if(idx==-1){
                    arr[i]++;
                    ans++;
                }
                else{
                    arr[idx]++;
                    if(arr[idx]==m){
                        arr[idx]=0;
                        ans++;
                    }
                }
            }
        }
    }
    return ans;
}

int main(){
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity = 1;
    printf("%d", max_fill(grid, capacity));
    return 0;
}

*/

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int max_fill(vector<vector<int>> grid, int capacity){
    int n = grid.size(), m = grid[0].size();
    int ans = 0;
    vector<int> arr(n, 0);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    for(int i = 0; i < n; i++){
        int cnt = count(grid[i].begin(), grid[i].end(), 1);
        pq.push({cnt, i});
    }

    while(!pq.empty