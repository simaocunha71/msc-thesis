    vector<vector<int>> ans;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                ans.push_back({i, j});
            }
        }
    }
    return ans;
}

int main() {
    vector<vector<int>> lst = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    int x = 1;
    vector<vector<int>> res = get_row(lst, x);
    for(int i = 0; i < res.size(); i++){
        printf("{%d, %d} ", res[i][0], res[i][1]);
    }
    return 0;
}
*/

int main() {
    vector<vector<int>> lst = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    int x = 1;
    vector<vector<int>> res = get_row(lst, x);
    for(int i = 0; i < res.size(); i++){
        printf("{%d, %d} ", res[i][0], res[i][1]);
    }
    return 0;
}
*/

int main() {
    vector<vector<int>> lst = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    int x = 1;
    vector<vector<int>> res = get_row(lst, x);
    for(int i = 0; i < res.size(); i++){
        printf("{%d, %d} ", res[i][0], res[i][1]);
    }
    return 0;
}
*/

int main() {
