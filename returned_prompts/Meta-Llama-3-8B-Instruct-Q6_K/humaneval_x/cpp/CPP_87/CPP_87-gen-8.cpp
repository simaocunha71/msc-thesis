    vector<vector<int>> result;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                vector<int> temp;
                temp.push_back(i);
                temp.push_back(j);
                result.push_back(temp);
            }
        }
    }
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b){
        if(a[0] == b[0]){
            return a[1] > b[1];
        }
        return a[0] < b[0];
    });
    return result;
}

B:
    vector<vector<int>> get_row(vector<vector<int>> lst, int x){
        vector<vector<int>> result;
        for(int i = 0; i < lst.size(); i++){
            for(int j = 0; j < lst[i].size(); j++){
                if(lst[i][j] == x){
                    result.push_back({i, j});
                }
            }
        }
        sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b){
            return make_tuple(a[0], -a[1]) < make_tuple(b[0], -b[1]);
        });
        return result;
    }

C:
    vector<vector<int>> get_row(vector<vector<int>> lst, int x){
        vector<vector<int>> result;
        for(auto i = 0; i < lst.size(); i++){
            for(auto j = 0; j < lst[i].size(); j++){
                if(lst[i][j] == x){
                    result.push_back({i, j});
                }
            }
        }
        sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b){
            return make_tuple(a[0], -a[1]) < make_tuple(b[0], -b[1]);
        });
        return result;
    }

D:
    vector<vector<int>> get_row(vector<vector<int>> lst, int x){
        vector<vector<int>> result;
        for(auto& row : lst){
            for(auto& element : row){
                if(element == x){
                    result.push_back({std::distance(lst.begin(), std::find_if(lst.begin(), lst.end(), [&](const auto& r) { return &r == &row; })),
 std::distance(row.begin(), std::find_if(row.begin(), row