
```
#include<bits/stdc++.h>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){

    set<int> st;
    for(int i:l1)st.insert(i);
    for(int i:l2)st.insert(i);
    vector<int> res;
    for(int i:st)res.push_back(i);
    sort(res.begin(),res.end());
    res.erase(unique(res.begin(),res.end()),res.end());
    return res;
}
int main(){
    vector<int> l1={1, 4, 3, 34, 653, 2, 5};
    vector<int> l2={5, 7, 1, 5, 9, 653, 121};
    vector<int> res=common(l1,l2);
    for(int i:res)printf("%d ",i);
    return 0;
}
```

```
#include<bits/stdc++.h>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    set<int> st;
    st.insert