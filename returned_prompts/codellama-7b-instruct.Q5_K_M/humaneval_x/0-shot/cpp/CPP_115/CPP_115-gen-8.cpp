    for(int i=0;i<grid.size();i++){
        for(int j=0;j<grid[0].size();j++){
            if(grid[i][j]==1){
                int count=1;
                int index=0;
                for(int k=i;k<grid.size();k++){
                    if(grid[k][j]==1)
                        count++;
                    else{
                        if(count>index){
                            index=count;
                            i=k;
                        }
                        break;
                    }
               