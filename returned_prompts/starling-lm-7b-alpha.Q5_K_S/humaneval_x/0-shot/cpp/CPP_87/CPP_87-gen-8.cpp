    vector<vector<int>> res;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i].size() == 0) continue;
        auto it = find(begin(lst[i]), end(lst[i]), x);
        if(it == end(lst[i])) continue;
        res.push_back({i, distance(begin(lst[i]), it)});
    }
    res.sort([](const vector<int>& a, const vector<int>& b){
        return a[0] < b[0];
    });
    return res;
}
int main(){
    vector<vector<int>> v = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    for(auto vv: get_row(v, 1)) printf("%d, %d\n", vv[0], vv[1]);
}

*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<vector<int>> get_row(vector<vector<int>> lst, int x){
    vector<vector<int>> res;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i].size() == 0) continue;
        auto it = find(begin(lst[i]), end(lst[i]), x);
        if(it == end(lst[i])) continue;
        res.push_back({i, distance(begin(lst[i]), it)});
    }
    sort(begin(res), end(res));
    for(auto& v: res) sort(begin(v), end(v), greater<int>());
    return res;
}
int main(){
    vector<vector<int>> v = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4,5,1}};
    for(auto vv: get_row(v, 1)) printf("%d, %d\n",