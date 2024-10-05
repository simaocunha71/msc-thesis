    if(k==0) return vector<int>();
    if(k==1) return vector<int>(1,grid[0][0]);
    int mn=grid[0][0];
    for(int i=0;i<grid.size();++i){
        for(int j=0;j<grid[i].size();++j){
            if(grid[i][j]<mn){
                mn=grid[i][j];
                r=i;
                c=j;
            }
        }
    }
    vector<int> res;
    res.push_back(mn);
    grid[r][c]=0;
    res=minPath(grid,k-1);
    grid[r][c]=mn;
    return res;
B:
    if(k==0) return vector<int>();
    if(k==1) return vector<int>(1,grid[0][0]);
    vector<int> res=minPath(grid,k-1);
    int mn=grid[0][0];
    for(int i=0;i<grid.size();++i){
        for(int j=0;j<grid[i].size();++j){
            if(grid[i][j]<mn){
                mn=grid[i][j];
                r=i;
                c=j;
            }
        }
    }
    if(res.size()<k-1){
        res.push_back(mn);
        grid[r][c]=0;
        res=minPath(grid,k-1);
        grid[r][c]=mn;
    }
    return res;
}
int main(){
    vector<vector<int>> grid={{1,2,3},{4,5,6},{7,8,9}};
    int k;
    cin >> k;
    vector<int> res=minPath(grid,k);
    for(auto i:res) cout << i << " ";
    cout << endl;
}

*/























