    vector<vector<int>> ans;
    vector<int> temp;
    for (int i = 0; i < lst.size(); i++) {
        temp.clear();
        for (int j = 0; j < lst[i].size(); j++) {
            if (lst[i][j] == x) {
                temp.push_back(i);
                temp.push_back(j);
                goto A;
            }
        }
    }
    ans.push_back(temp);
    return ans;
}

int main() {
    vector<vector<int>> lst = {{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 1, 6}, {1, 2, 3, 4, 5, 1}};
    vector<vector<int>> ans = get_row(lst, 1);
    for (int i = 0; i < ans.size(); i++) {
        for (int j = 0; j < ans[i].size(); j++) {
            printf("%d ", ans[i][j]);
        }
        printf("\n");
    }
    return 0;
}























































































































































































































