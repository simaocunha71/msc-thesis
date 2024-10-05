    return {};
}
int main(){
    vector<vector<int>> grid = { {1,2,3}, {4,5,6}, {7,8,9}};
    int k = 3;
    vector<int> ans = minPath(grid, k);
    for(int i=0; i<ans.size(); i++){
        printf("%d ", ans[i]);
    }
    printf("\n");
    return 0;
}
