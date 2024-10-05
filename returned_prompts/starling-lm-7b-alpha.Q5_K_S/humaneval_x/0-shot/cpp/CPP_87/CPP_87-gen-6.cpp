vector<vector<int>> result;
for (size_t i = 0; i < lst.size(); i++) {
    for (size_t j = 0; j < lst[i].size(); j++) {
        if (lst[i][j] == x) {
            result.push_back({i, j});
        }
    }
}
result.sort([](const vector<int>& a, const vector<int>& b) {
    return a[0] < b[0];
});
for (size_t i = 0; i < result.size(); i++) {
    result[i].push_back(result[i][1]);
    result[i].pop_back();
}
result.sort([](const vector<int>& a, const vector<int>& b) {
    return a[1] > b[1];
});
return result;
}

int main() {
    auto r = get_row({{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 1, 6}, {1, 2, 3, 4, 5, 1}}, 1);
    for (size_t i = 0; i < r.size(); i++) {
        printf("(%d, %d)\n", r[i][0], r[i][1]);
    }
    return 0;
}












































































































































































