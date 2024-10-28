    int n = grid.size();
    int m = grid[0].size();
    vector<vector<int>> dist(n, vector<int>(m, INT_MAX));
    vector<int> result;
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;

    pq.push({grid[0][0], {0, 0}});
    dist[0][0] = grid[0][0];
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};

    while(!pq.empty()){
        pair<int, pair<int, int>> temp = pq.top();
        pq.pop();

        int x = temp.second.first;
        int y = temp.second.second;

        if(temp.first > dist[x][y]) continue;

        if(result.size() == k){
            break;
        }

        result.push_back(grid[x][y]);

        for(int i = 0; i < 4; i++){
            int newX = x + dx[i];
            int newY = y + dy[i];

            if(newX >= 0 && newX < n && newY >= 0 && newY < m){
                if(dist[newX][newY] > dist[x][y] + grid[newX][newY]){
                    dist[newX][newY] = dist[x][y] + grid[newX][newY];
                    pq.push({dist[newX][newY], {newX, newY}});
                }
            }
        }
    }

    return result;
}


