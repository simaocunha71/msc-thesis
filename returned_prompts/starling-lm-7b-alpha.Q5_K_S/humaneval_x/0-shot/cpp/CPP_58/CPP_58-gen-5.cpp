
#include<bits/stdc++.h>
using namespace std;

vector<int> common(vector<int> l1,vector<int> l2){
    set<int> s;
    vector<int> ans;
    for(int i=0;i<l1.size();i++){
        s.insert(l1[i]);
    }
    for(int i=0;i<l2.size();i++){
        if(s.count(l2[i])>0){
            s.erase(l2[i]);
            ans.push_back(l2[i]);
        }
    }
    return ans;
}

int main(){
    vector<int> l1={1, 4, 3, 34, 653, 2, 5};
    vector<int> l2={5, 7, 1, 5, 9, 653,