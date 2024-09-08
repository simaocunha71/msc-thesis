#include<stdio.h>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    set<int> s1(l1.begin(),l1.end());
    set<int> s2(l2.begin(),l2.end());
    vector<int> v;
    for(auto it=s1.begin();it!=s1.end();it++){
        if(s2.find(*it)!=s2.end()){
            v.push_back(*it);
        }
    }
    sort(v.begin(),v.end());
    return v;
}
