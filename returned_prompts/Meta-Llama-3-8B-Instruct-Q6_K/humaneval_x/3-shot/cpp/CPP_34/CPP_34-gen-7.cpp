    vector<int> result;
    for(int i=0;i<l.size();i++)
    {
        if(find(result.begin(),result.end(),l[i]) == result.end())
        {
            result.push_back(l[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}
// or
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> unique(vector<int> l){
    set<int> s(l.begin(),l.end());
    vector<int> result(s.begin(),s.end());
    sort(result.begin(), result.end());
    return result;
}
// or
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> unique(vector<int> l){
    vector<int> result;
    for(auto i:l)
    {
        if(find(result.begin(),result.end(),i) == result.end())
        {
            result.push_back(i);
        }
    }
    sort(result.begin(), result.end());
    return result;
}