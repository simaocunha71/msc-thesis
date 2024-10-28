    return vector<int>();
}

int main(){
    vector<vector<int>> grid;
    int k;
    vector<int> result;
    result = minPath(grid, k);
    for(int i=0; i<result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}