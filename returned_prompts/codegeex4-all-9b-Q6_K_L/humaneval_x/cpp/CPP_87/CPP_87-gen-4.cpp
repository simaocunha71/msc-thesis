#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<vector<int>> get_row(vector<vector<int>> lst, int x){
    vector<vector<int>> coords;
    for (int i = 0; i < lst.size(); i++) {
        for (int j = 0; j < lst[i].size(); j++) {
            if (lst[i][j] == x) {
                coords.push_back({i, j});
            }
        }
    }
    sort(coords.begin(), coords.end());
    for (int i = 0; i < coords.size(); i++) {
        for (int j = i + 1; j < coords.size(); j++) {
            if (coords[i][0] == coords[j][0] && coords[i][1] < coords[j][1]) {
                swap(coords[i], coords[j]);
            }
        }
    }
    return coords;
}