    int n = grid.size();
    vector<int> res;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(res.size() < k){
                res.push_back(grid[i][j]);
            }else{
                break;
            }
        }
    }
    return res;
}

int main(){
    vector<vector<int>> grid = {{1,2,3},{4,5,6},{7,8,9}};
    int k = 3;
    vector<int> res = minPath(grid, k);
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    printf("\n");
    return 0;
}*/



