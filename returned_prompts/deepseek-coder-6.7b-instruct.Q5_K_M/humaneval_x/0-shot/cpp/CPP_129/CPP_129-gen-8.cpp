    return vector<int>();
}

int main() {
    vector<vector<int>> grid = {{1,2,3}, {4,5,6}, {7,8,9}};
    int k = 3;
    vector<int> res = minPath(grid, k);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}
*/

/*
