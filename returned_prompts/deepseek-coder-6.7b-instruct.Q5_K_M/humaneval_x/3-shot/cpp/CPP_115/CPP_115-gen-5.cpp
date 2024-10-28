    int i, j, ans = 0, cur = 0;
    for(i=0; i<grid.size(); i++){
        for(j=0; j<grid[0].size(); j++){
            if(grid[i][j] == 1){
                if(cur < capacity){
                    cur++;
                    ans++;
                }
            } else {
                cur = 0;
            }
        }
        cur = 0;
    }
    return ans;
}


