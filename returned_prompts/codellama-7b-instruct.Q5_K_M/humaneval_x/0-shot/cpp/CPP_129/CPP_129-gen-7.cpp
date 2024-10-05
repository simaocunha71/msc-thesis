    return {};
}

int main(){
    vector<vector<int>> grid = {{1,2,3}, {4,5,6}, {7,8,9}};
    int k = 3;
    vector<int> res = minPath(grid, k);
    for(auto i : res)
        printf("%d ", i);
    return 0;
}
