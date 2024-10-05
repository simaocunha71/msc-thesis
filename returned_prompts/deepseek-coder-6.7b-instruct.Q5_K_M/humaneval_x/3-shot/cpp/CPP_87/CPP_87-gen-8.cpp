    vector<vector<int>> coordinates;
    for (int i = 0; i < lst.size(); i++) {
        for (int j = 0; j < lst[i].size(); j++) {
            if (lst[i][j] == x) {
                coordinates.push_back({i, j});
            }
        }
    }
    sort(coordinates.begin(), coordinates.end(), [](const auto &a, const auto &b) {
        if (a[0] == b[0]) {
            return a[1] > b[1];
        }
        return a[0] < b[0];
    });
    return coordinates;
}

