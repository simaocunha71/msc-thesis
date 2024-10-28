    vector<vector<int>> all_paths;
    vector<int> current_path;
    int i,j;

    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    {
        current_path.push_back(grid[i][j]);
        all_paths.push_back(current_path);
        current_path.pop_back();
    }

    sort(all_paths.begin(),all_paths.end());

    vector<int> result;
    int total_size=all_paths.size();
    int path_size=k;
    if (total_size<path_size)
    {
        return result;
    }
    if (total_size==path_size)
    {
        return all_paths[0];
    }
    int i_max=path_size/2;
    int i_min=total_size-path_size+1;
    for (i=i_min;i<=i_max;i++)
    {
        if (all_paths[i]!=all_paths[i_min])
        {
            result=all_paths[i];
            break;
        }
    }
    return result;
}












































































































































































































