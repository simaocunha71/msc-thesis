
    vector<vector<int>> result;

    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                result.push_back({i, j});
            }
        }
    }

    // Sorting the vector of vectors by rows in ascending order.
    sort(result.begin(), result.end());

    // Sorting coordinates of the row by columns in descending order.
    for(auto &row: result){
        sort(row.rbegin(), row.rend());
    }

    return result;
}


int main(){
    vector<vector<int>> lst = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    int x = 1;

    vector<vector<int>> res = get_row(lst, x);

    for(int i = 0; i < res.size(); i++){
        printf("{%d, %d} ", res[i][0], res[i][1]);
    }

    return 0;
}
*/




// Answer:
/*
