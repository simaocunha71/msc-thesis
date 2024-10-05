    int i,j,n;
    vector<vector<int>> all_paths;
    vector<int> one_path;
    int curr_x,curr_y;
    int next_x,next_y;
    int curr_number;
    int next_number;
    int counter=0;
    vector<int> result;
    bool finished;

    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    {
        curr_x=i;
        curr_y=j;
        curr_number=grid[i][j];
        counter=0;
        finished=false;
        while(!finished)
        {
            counter+=1;
            for (n=-1;n<=1;n++)
            {
                next_x=curr_x+n;
                next_y=curr_y;
                if (next_x<0 || next_y<0 || next_x>=grid.size() || next_y>=grid[0].size())
                continue;
                next_number=grid[next_x][next_y];
                if (next_number!=0)
                {
                    one_path.push_back(curr_number);
                    if (counter==k)
                    {
                    finished=true;
                    break;
                    }
                    curr_x=next_x;
                    curr_y=next_y;
                    curr_number=next_number;
                    counter=0;
                }
            }
        }
        if (finished)
        all_paths.push_back(one_path);
        one_path.clear();
    }

    result.clear();
    for (i=0;i<all_paths.size();i++)
    for (j=0;j<all_paths[i].size();j++)
    if (result.size()<k)
    result.push_back(all_paths[i][j]);

    return result;
}













