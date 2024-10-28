    vector<vector<pair<int, int>>> dist(grid.size(), vector<pair<int, int>>(grid.size()));
    for(int i = 0; i < grid.size(); i++) dist[i][i] = {0, grid[i][i]};

    for(int i = 0; i < grid.size(); i++)
    for(int j = 0; j < grid[i].size(); j++)
    if(i > 0) dist[i][j] = min(dist[i][j], dist[i-1][j]);
    if(j > 0) dist[i][j] = min(dist[i][j], dist[i][j-1]);

    vector<vector<pair<int, int>>> prev(grid.size(), vector<pair<int, int>>(grid.size(), {-1, -1}));

    for(int i = 0; i < grid.size(); i++)
    for(int j = 0; j < grid[i].size(); j++)
    if(grid[i][j] == 1) dist[i][j] = {0, grid[i][j]};

    vector<vector<int>> dists(grid.size(), vector<int>(grid.size()));
    for(int i = 0; i < grid.size(); i++)
    for(int j = 0; j < grid[i].size(); j++)
    if(i < grid.size()-1 && dist[i][j] < dist[i+1][j])
    dists[i][j] = dist[i][j].second, dist[i][j] = dist[i+1][j];
    prev[i][j] = {i, j};
    for(int i = 0; i < grid.size(); i++)
    for(int j = 0; j < grid[i].size(); j++)
    if(j < grid[i].size()-1 && dist[i][j] < dist[i][j+1])
    dists[i][j] = dist[i][j].second, dist[i][j] = dist[i][