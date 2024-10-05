    vector<vector<int>> ret;
    for(int i = 0; i < lst.size(); i++) {
        if(lst[i].size() == 0) continue;
        if(lst[i][0] == x) {
            ret.push_back(vector<int>({i, lst[i].size() - 1}));
        }
    }
    return ret;
}

int main() {
    vector<vector<int>> lst = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    for(auto v : get_row(lst, 1)) printf("(%d, %d)\n", v[0], v[1]);
    return 0;
}


*/
#include<bits/stdc++.h>
using namespace std;

int main() {
    vector<vector<int>> lst = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    vector<vector<int>> ret = get_row(lst, 1);
    for(auto v : ret) printf("(%d, %d)\n", v[0], v[1]);
    return 0;
}

vector<vector<int>> get_row(vector<vector<int>> lst, int x){
    vector<vector<int>> ret;
    for(int i = 0; i < lst.size(); i++) {
        if(lst[i].size() == 0) continue;
        if(lst[i][0] == x) {
            ret.push_back(vector<int>({i, lst[i].size() - 1}));
        }
    }
    sort(ret.begin(), ret.end());
    return ret;
}













































