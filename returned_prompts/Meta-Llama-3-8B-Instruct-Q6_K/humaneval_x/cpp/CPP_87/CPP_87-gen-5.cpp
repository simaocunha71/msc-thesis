    vector<vector<int>> res;
    vector<pair<int, int>> coords;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                coords.push_back({i, j});
            }
        }
    }
    sort(coords.begin(), coords.end());
    for(auto coord : coords){
        res.push_back({coord.first, coord.second});
    }
    return res;
}
B:
    vector<vector<int>> get_row(vector<vector<int>> lst, int x){
        vector<vector<int>> res;
        for(int i = 0; i < lst.size(); i++){
            for(int j = 0; j < lst[i].size(); j++){
                if(lst[i][j] == x){
                    res.push_back({i, j});
                }
            }
        }
        sort(res.begin(), res.end());
        return res;
    }
C:
    vector<vector<int>> get_row(vector<vector<int>> lst, int x){
        vector<vector<int>> res;
        for(int i = 0; i < lst.size(); i++){
            for(int j = 0; j < lst[i].size(); j++){
                if(lst[i][j] == x){
                    res.push_back({i, j});
                }
            }
        }
        sort(res.begin(), res.end(), [](const auto& a, const auto& b){
            if(a[0] == b[0]) return a[1] > b[1];
            return a[0] < b[0];
        });
        return res;
    }
D:
    vector<vector<int>> get_row(vector<vector<int>> lst, int x){
        vector<vector<int>> res;
        for(auto &row : lst){
            for(auto &col : row){
                if(col == x){
                    res.push_back({find(row.begin(), row.end(), x) - row.begin(), row.size() - 1});
                }
            }
        }
        sort(res.begin(), res.end());
        return res;
    }
E:
    vector<vector<int>> get_row(vector<vector<int>> lst, int x){
        vector<pair<int, int>> coords;
        for(int i = 0; i < lst.size(); i++){
            for(int j = 0; j < lst[i].size(); j++){
                if(lst[i][j] == x){
                    coords.push_back({i, j