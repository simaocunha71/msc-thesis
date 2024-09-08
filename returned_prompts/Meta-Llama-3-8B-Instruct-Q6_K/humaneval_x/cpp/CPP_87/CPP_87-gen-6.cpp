vector<vector<int>> res;
for (int i = 0; i < lst.size(); i++) {
    for (int j = 0; j < lst[i].size(); j++) {
        if (lst[i][j] == x) {
            res.push_back({i, j});
        }
    }
}
sort(res.begin(), res.end(), [](const vector<int>& a, const vector<int>& b) {
    return a[0] < b[0];
});
for (auto& coord : res) {
    sort(coord.begin(), coord.end(), [](int a, int b) {
        return a > b;
    });
}
return res;
}
int main() {
    vector<vector<int>> lst = {{1,2,3,4,5,6},{1,2,3,4,1,6},{1,2,3,4,5,1}};
    int x = 1;
    vector<vector<int>> res = get_row(lst, x);
    for (auto& coord : res) {
        printf("(%d, %d)\n", coord[0], coord[1]);
    }
    return 0;
}
B:
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x) {
    vector<vector<int>> res;

    // Find all positions where x is present
    for (int i = 0; i < lst.size(); i++) {
        for (int j = 0; j < lst[i].size(); j++) {
            if (lst[i][j] == x) {
                res.push_back({i, j});
            }
        }
    }

    // Sort by rows in ascending order
    sort(res.begin(), res.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });

    // Sort by columns in descending order
    for (auto& coord : res) {
        sort(coord.begin(), coord.end(), [](int a, int b) {
            return a > b;
        });
    }

    return res;
}

int main() {
    vector<vector<int>> lst = {{1,2,3,4,5,6},{1,2,3,4,1,6},{1,2,3,4,5,1}};
    int x = 1;

    vector<vector<int>> res =