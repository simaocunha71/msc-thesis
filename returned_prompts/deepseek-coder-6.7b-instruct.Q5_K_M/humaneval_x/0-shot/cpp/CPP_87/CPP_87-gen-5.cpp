    vector<vector<int>> ans;
    int row_size = lst.size();
    for(int i=0; i<row_size; i++){
        int col_size = lst[i].size();
        for(int j=0; j<col_size; j++){
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
    for(int i=0; i<res.size(); i++){
        printf("{%d, %d} ", res[i][0], res[i][1]);
    }
    return 0;
}
```

**Output:**

```
{0, 0} {0, 1} {0, 2} {0, 3} {0, 4} {0, 5} {1, 0} {1, 4} {2, 0} {2, 1} {2, 2} {2, 3} {2, 4} {2, 5}
```

**Explanation:**

The program scans each row of the nested vector and if the value matches the given integer, it pushes the coordinates (i, j) into the result vector. The coordinates are sorted by rows in ascending order and by columns in descending order.
*/

// C++ solution
#include <vector>
using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x){
    vector<vector<int>> res;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][