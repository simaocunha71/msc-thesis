    vector<vector<int>> res;
    int i,j;
    for(i=0;i<lst.size();i++)
        for(j=0;j<lst[i].size();j++)
            if(lst[i][j]==x)
                res.push_back({i,j});
    sort(res.begin(),res.end());
    return res;
}
int main(){
    vector<vector<int>> lst={
        {1,2,3,4,5,6},
        {1,2,3,4,1,6},
        {1,2,3,4,5,1}
    };
    vector<vector<int>> res=get_row(lst,1);
    for(int i=0;i<res.size();i++)
        printf("%d %d\n",res[i][0],res[i][1]);
    return 0;
}

*/
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x) {
    vector<vector<int>> res;
    for (int i = 0; i < lst.size(); i++) {
        auto it = lower_bound(lst[i].begin(), lst[i].end(), x);
        if (it != lst[i].end() && *it == x) {
            res.push_back({i, distance(lst[i].begin(), it)});
        }
    }
    sort(res.begin(), res.end());
    return res;
}

int main() {
    vector<vector<int>> lst = {{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 1, 6}, {1, 2, 3, 4, 5, 1}};
    vector<vector<int>> res = get_row(lst, 1);
    for (int i = 0; i < res.size(); i++) {
        cout << res[i][0] << " " <<