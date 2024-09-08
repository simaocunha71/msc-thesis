    vector<vector<int>> result;

    // Sort lst by rows in ascending order
    sort(lst.begin(), lst.end());

    for(int i = 0; i < lst.size(); i++){
        // Sort each row by columns in descending order
        sort(lst[i].begin(), lst[i].end(), greater<int>());
        for(int j = 0; j < lst[i].size(); j++){
            // Check if element is equal to x
            if(lst[i][j] == x){
                result.push_back({i, j});
            }
        }
    }

    return result;
}