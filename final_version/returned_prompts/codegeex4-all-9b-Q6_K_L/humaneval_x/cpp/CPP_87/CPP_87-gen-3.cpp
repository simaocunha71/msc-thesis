#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x) {
    vector<vector<int>> result;
    for (int i = 0; i < lst.size(); i++) {
        for (int j = 0; j < lst[i].size(); j++) {
            if (lst[i][j] == x) {
                result.push_back({i, j});
            }
        }
    }

    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a[0] != b[0]) {
            return a[0] < b[0];
        } else {
            return a[1] > b[1];
        }
    });

    return result;
}

int main() {
    vector<vector<int>> lst = {{1, 2, 3, 4, 5, 6},
                               {1, 2, 3, 4, 1, 6},
                               {1, 2, 3, 4, 5, 1}};
    int x = 1;
    vector<vector<int>> result = get_row(lst, x);
    for (const auto& v : result) {
        cout << "{" << v[0] << ", " << v[1] << "} ";
    }
    cout << endl;
    return 0;
}

C:
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x) {
    vector<vector<int>> result;
    for (int i = 0; i < lst.size(); i++) {
        for (int j = 0; j < lst[i].size(); j++) {
            if (lst[i][j] == x) {
                result.push_back({i, j});
            }
        }
    }

    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a[0] != b[0]) {
            return a[0] < b[0];
        } else {
            return a[1] > b[1];
        }
    });

    return result;
}

int main() {
    vector<vector<int>> lst = {{1, 2, 3, 4, 5, 6},
                               {1, 2