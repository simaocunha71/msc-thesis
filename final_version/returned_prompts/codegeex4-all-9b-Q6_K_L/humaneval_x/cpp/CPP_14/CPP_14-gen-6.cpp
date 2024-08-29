```c++
#include<bits/stdc++.h>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> ans;
    for(int i=1;i<=str.size();i++){
        string sub = str.substr(0,i);
        ans.push_back(sub);
    }
    return ans;
}
int main(){
    vector<string> ans = all_prefixes("abc");
    for(auto i:ans) cout<<i<<" ";
    return 0;
}
```
