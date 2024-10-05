    if(lst.size()==0)return lst;
    sort(lst.begin(),lst.end());
    vector<int> ans;
    for(int i=0;i<lst.size();i+=2){
        ans.push_back(lst[i]);
    }
    for(int i=lst.size()-1;i>=0;i-=2){
        ans.push_back(lst[i]);
    }
    return ans;
}
int main(){
    vector<int> A={1, 2, 3, 4};
    vector<int> ans=strange_sort_list(A);
    for(auto a:ans){
        printf("%d ",a);
    }
    return 0;
}



*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4};
    auto res = strange_sort_vector(v);
    for (auto x : res) {
        cout << x << ' ';
    }
    return 0;
}

vector<int> strange_sort_vector(vector<int> v) {
    sort(v.begin(), v.end());
    vector<int> res;
    for (int i = 0; i < v.size(); i += 2) {
        res.push_back(v[i]);
    }
    for (int i = v.size() - 1; i >= 0; i -= 2) {
        res.push_back(v[i]);
    }
    return res;
}



















































































































