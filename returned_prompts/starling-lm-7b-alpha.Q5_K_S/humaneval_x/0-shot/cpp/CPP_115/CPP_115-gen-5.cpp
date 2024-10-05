    int r = grid.size(),c = grid[0].size();
    int cnt = 0;
    for(int i = 0;i < r;i++)
        for(int j = 0;j < c;j++)
            if(grid[i][j])
                grid[i][j]--;
    while(true){
        bool ok = false;
        for(int i = 0;i < r;i++)
            for(int j = 0;j < c;j++)
                if(grid[i][j]){
                    ok = true;
                    grid[i][j]--;
                    if(grid[i][j] == 0)
                        grid[i][j] = -1;
                }
        for(int i = r - 1;i >= 0;i--)
            for(int j = c - 1;j >= 0;j--)
                if(grid[i][j] == -1)
                    grid[i][j] = capacity;
        cnt++;
        if(!ok)
            break;
    }
    return cnt;
}

int main() {
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    printf("%d\n",max_fill(grid,1));
}


















































































































































































