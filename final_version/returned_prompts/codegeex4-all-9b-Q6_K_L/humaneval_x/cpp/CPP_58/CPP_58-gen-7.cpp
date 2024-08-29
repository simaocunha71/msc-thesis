#include<stdio.h>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    set<int> s1,lst;
    for(int i=0;i<l1.size();i++)
        s1.insert(l1[i]);
    for(int i=0;i<l2.size();i++){
        if(s1.find(l2[i])!=s1.end())
            lst.insert(l2[i]);
    }
    vector<int> l3;
    for(auto it=lst.begin();it!=lst.end();it++)
        l3.push_back(*it);
    sort(l3.begin(),l3.end());
    return l3;
}

B:
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    set<int> s1,lst;
    for(int i=0;i<l1.size();i++)
        s1.insert(l1[i]);
    for(int i=0;i<l2.size();i++){
        if(s1.find(l2[i])!=s1.end())
            lst.insert(l2[i]);
    }
    vector<int> l3;
    for(auto it=lst.begin();it!=lst.end();it++)
        l3.push_back(*it);
    sort(l3.begin(),l3.end());
    return l3;
}

C:
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    set<int> s1,lst;
    for(int i=0;i<l1.size();i++)
        s1.insert(l1[i]);
    for(int i=0;i<l2.size();i++){
        if(s1.find(l2[i])!=s1.end())
            lst.insert(l2[i]);
    }
    vector<int> l3;
    for(auto it=lst.begin();it!=lst.end();it++)
        l3.push_back(*it);
    sort(l3.begin(),l3.end());
    return l3;
}

D:
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    set<int> s1,lst;
    for(int i=0;i<l1.size();i++)
        s1.insert(l1[i]);
    for(int i=0;i<l