    int count=0;
    for  (int i=0;i<grid.size();i++)
        for  (int j=0;j<grid[0].size();j++)
            if  (grid[i][j]==1)
            {
                count+=1;
                if  (count%capacity==0)
                    count+=1;
            }
    return count;
}


