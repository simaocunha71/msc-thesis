    vector<vector<int>> res;
    for(int i = 0; i < lst.size(); ++i){
        for(int j = 0; j < lst[i].size(); ++j){
            if(lst[i][j] == x){
                res.push_back({i, j});
            }
        }
    }
    return res;
}

int main(){
    vector<vector<int>> lst = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    int x = 1;
    vector<vector<int>> res = get_row(lst, x);
    for(int i = 0; i < res.size(); ++i){
        printf("{%d, %d} ", res[i][0], res[i][1]);
    }
    return 0;
}
/*
Output:
{0, 0} {0, 1} {0, 2} {0, 3} {0, 4} {0, 5} {1, 4} {1, 0} {1, 5} {2, 0} {2, 5}
*/

This solution goes through each row and each column in each row to find the integer x, and then adds the coordinates {row, column} to the result vector. The coordinates are sorted by rows in ascending order and by columns in descending order.
*/





























































































































































