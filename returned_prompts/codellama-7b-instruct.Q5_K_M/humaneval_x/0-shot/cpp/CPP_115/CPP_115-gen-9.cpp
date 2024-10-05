    int m = grid.size();
    int n = grid[0].size();
    int i = 0,j = 0;
    int cnt = 0;
    while(i<m){
        while(j<n){
            if(grid[i][j]==1){
                cnt++;
                grid[i][j] = 0;
            }
            if(j==n-1){
                i++;
                j = 0;
            }
            else{
                j++;
            }
        }
        while(i<m && grid[i][0]==0){
            i++;
        }
        if(i==m){
            break;
        }
        j = 0;
    }
    if(cnt>capacity){
        cnt = cnt - capacity;
        goto A;
    }
    else{
        return cnt;
    }
}

int main(){
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    printf("%d\n",max_fill(grid,1));
    return 0;
}



