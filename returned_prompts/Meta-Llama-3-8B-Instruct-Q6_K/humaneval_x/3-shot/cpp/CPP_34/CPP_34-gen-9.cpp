    vector<int> result;
    for (auto x : l)
    {
        if (find(result.begin(), result.end(), x) == result.end())
        {
            result.push_back(x);
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
    set<int> s(l.begin(), l.end());
    vector<int> result(s.begin(), s.end());
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
    for (auto x : l)
    {
        if (result.empty() || x > result.back())
        {
            result.push_back(x);
        }
    }
    sort(result.begin(), result.end());
    return result;
}