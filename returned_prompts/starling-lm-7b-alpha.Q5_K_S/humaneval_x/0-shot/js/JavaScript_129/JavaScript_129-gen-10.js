    for(let i=0;i<grid.length;i++) {
        for(let j=0;j<grid[i].length;j++) {
            if(grid[i][j] <= k) {
                let curr = grid[i][j];
                let res = [curr];
                if(i>0) {
                    res.push(grid[i-1][j]);
                    if(grid[i-1][j]+grid[i-1][j+1]+grid[i-1][j-1] == curr) {
                        continue A;
                    }
                }
                if(j>0) {
                    res.push(grid[i][j-1]);
                    if(grid[i][j-1]+grid[i][j-1]+grid[i][j-2] == curr) {
                        continue A;
                    }
                }
                if(i<grid.length-1) {
                    res.push(grid[i+1][j]);
                    if(grid[i+1][j]+grid[i+1][j+1]+grid[i+1][j-1] == curr) {
                        continue A;
                    }
                }
                if(j<grid[i].length-1) {
                    res.push(grid[i][j+1]);
                    if(grid[i][j+1]+grid[i][j+1]+grid[i][j+2] == curr) {
                        continue A;
                    }
                }
                return res;
            }
        }
    }
}




















































































































