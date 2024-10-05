    vector<int> result;
    for (int i=0;i<l.size();i++)
    {
        bool found = false;
        for (int j=0;j<result.size();j++)
        {
            if (l[i]==result[j])
            {
                found = true;
                break;
            }
        }
        if (!found)
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
    vector<int> result;
    for (int i=0;i<l.size();i++)
    {
        if (find(result.begin(), result.end(), l[i]) == result.end())
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
    sort(l.begin(), l.end());
    l.erase(unique(l.begin(), l.end()), l.end());
    return l;
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
    set<int> s;
    for (int i=0;i<l.size();i++)
    {
        s.insert(l[i]);
    }
    for (set<int>::iterator it=s.begin();it!=s.end();it++)
    {
        result.push_back(*it);
    }
    sort(result.begin(), result.end());
    return result;
} // best solution


