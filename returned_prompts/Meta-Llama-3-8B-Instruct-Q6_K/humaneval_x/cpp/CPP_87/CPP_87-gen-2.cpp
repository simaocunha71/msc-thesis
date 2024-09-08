    vector<vector<int>> result;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                result.push_back({i, j});
            }
        }
    }
    sort(result.begin(), result.end());
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] > b[1];
    });
    return result;
}

B:
    vector<vector<int>> result;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                result.push_back({i, j});
            }
        }
    }
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        if(a[0] == b[0]){
            return a[1] > b[1];
        }
        return a[0] < b[0];
    });
    return result;

C:
    vector<vector<int>> result;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                result.push_back({i, j});
            }
        }
    }
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        return make_pair(a[0], -a[1]) < make_pair(b[0], -b[1]);
    });
    return result;
}

D:
    vector<vector<int>> result;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                result.push_back({i, j});
            }
        }
    }
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        return tie(a[0], a[1]) < tie(b[0], b[1]);
    });
    return result;
}