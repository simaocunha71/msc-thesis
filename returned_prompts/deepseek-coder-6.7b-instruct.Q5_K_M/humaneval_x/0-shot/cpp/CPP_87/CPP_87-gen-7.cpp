    vector<vector<int>> res;
    for(int i=0; i<lst.size(); i++){
        for(int j=0; j<lst[i].size(); j++){
            if(lst[i][j] == x){
                res.push_back({i, j});
            }
        }
    }
    for(int i=0; i<res.size(); i++){
        for(int j=0; j<res.size()-i-1; j++){
            if(res[j][0] > res[j+1][0]){
                swap(res[j], res[j+1]);
            }
            else if(res[j][0] == res[j+1][0] && res[j][1] < res[j+1][1]){
                swap(res[j], res[j+1]);
            }
        }
    }
    return res;
}

int main(){
    vector<vector<int>> lst = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    int x = 1;
    vector<vector<int>> res = get_row(lst, x);
    for(int i=0; i<res.size(); i++){
        printf("{%d, %d} ", res[i][0], res[i][1]);
    }
    return 0;
}
```

The function `get_row` first loops through the given 2D vector to find the integers `x`, and then stores the coordinates as a 2D vector `res`. After that, it sorts the coordinates by rows in ascending order and by columns in descending order. Finally, it returns the sorted `res`.

In the `main` function, it calls the function `get_row` with the given parameters and prints the returned result.

Note that this solution assumes that the rows and columns are 0-indexed.

Also, note that this solution uses the C++ standard library, so it may not work correctly if the C++ standard library is not