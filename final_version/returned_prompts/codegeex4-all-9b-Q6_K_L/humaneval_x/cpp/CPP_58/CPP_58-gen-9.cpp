#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    vector<int> l3;
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(l3));
    sort(l3.begin(),l3.end());
    l3.erase(unique(l3.begin(),l3.end()),l3.end());
    return l3;
}

B:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    vector<int> l3;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(l3));
    sort(l3.begin(),l3.end());
    l3.erase(unique(l3.begin(),l3.end()),l3.end());
    return l3;
}

C:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    vector<int> l3;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(l3));
    l3.erase(unique(l3.begin(),l3.end()),l3.end());
    return l3;
}

D:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    vector<int> l3;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(l3));
    set(l3.begin(),l3.end());
    return l3;
}

E:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> common(vector<int> l1,vector<int> l2){
    vector<int> l3;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(l3));
    set(l3.begin(),l3.end());
    sort(l3