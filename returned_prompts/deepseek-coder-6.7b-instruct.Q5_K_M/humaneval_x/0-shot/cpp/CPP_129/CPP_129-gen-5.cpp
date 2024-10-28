    return {1};
}

int main(){
    vector<vector<int>> grid = {{5,9,3}, {4,1,6}, {7,8,2}};
    int k = 1;
    vector<int> res = minPath(grid, k);
    for(auto i:res)
        printf("%d ", i);
    return 0;
}

