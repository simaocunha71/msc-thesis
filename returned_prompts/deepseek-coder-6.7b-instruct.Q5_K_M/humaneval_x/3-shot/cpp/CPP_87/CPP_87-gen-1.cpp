    vector<vector<int>> coords;
    for(int i=0; i<lst.size(); i++){
        for(int j=0; j<lst[i].size(); j++){
            if(lst[i][j] == x)
                coords.push_back(vector<int>{i, j});
        }
    }
    sort(coords.begin(), coords.end(), [](const vector<int> &a, const vector<int> &b){
        return a[0]<b[0] || (a[0]==b[0] && a[1]>b[1]);
    });
    return coords;
}


