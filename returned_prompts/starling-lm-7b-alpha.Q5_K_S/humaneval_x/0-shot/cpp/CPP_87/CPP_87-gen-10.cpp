    vector<vector<int>> result;
    for (int i = 0; i < lst.size(); i++) {
        for (int j = 0; j < lst[i].size(); j++) {
            if (lst[i][j] == x) {
                result.push_back({i, j});
            }
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<vector<int>> lst = {{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 1, 6}, {1, 2, 3, 4, 5, 1}};
    printf("Input: ");
    for (int i = 0; i < lst.size(); i++) {
        for (int j = 0; j < lst[i].size(); j++) {
            printf("%d ", lst[i][j]);
        }
        printf("\n");
    }
    printf("Output: ");
    for (auto e : get_row(lst, 1)) {
        printf("%d, %d, ", e[0], e[1]);
    }
    printf("\n");
    return 0;
}








































































































































































































