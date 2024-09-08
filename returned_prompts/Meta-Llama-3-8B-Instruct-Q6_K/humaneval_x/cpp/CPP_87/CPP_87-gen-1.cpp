vector<vector<int>> result;
for(int i = 0; i < lst.size(); i++){
    for(int j = 0; j < lst[i].size(); j++){
        if(lst[i][j] == x){
            result.push_back({i, j});
        }
    }
}
sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b){
    if(a[0] == b[0]){
        return a[1] > b[1];
    }
    return a[0] < b[0];
});
return result;
}

// Test
int main() {
    vector<vector<int>> lst = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    int x = 1;
    vector<vector<int>> result = get_row(lst, x);
    for(auto v : result){
        printf("(%d, %d)\n", v[0], v[1]);
    }
    return 0;
}

Output:
(0, 0)
(1, 4)
(1, 0)
(2, 5)
(2, 0)

Explanation: The function get_row() finds all the occurrences of the number x in the given 2D vector lst. It then sorts these coordinates by their row numbers in ascending order, and within each row, it sorts the column numbers in descending order. The result is a vector of vectors where each inner vector represents a coordinate (row, column) of the number x. The test case demonstrates this functionality. It prints the coordinates where the number 1 is found in the given 2D vector. The output shows that the number 1 is found at coordinates (0, 0), (1, 4), (1, 0), (2, 5), and (2, 0).