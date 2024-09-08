#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    int n = lst.size();
    vector<int> res;
    if(n == 0){
        return res;
    }
    sort(lst.begin(), lst.end());
    int i = 0;
    while(i < n){
        res.push_back(lst[i]);
        i += 2;
    }
    i = 1;
    while(i < n){
        res.push_back(lst[i]);
        i += 2;
    }
    return res;

B:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    int n = lst.size();
    vector<int> res;
    if(n == 0){
        return res;
    }
    sort(lst.begin(), lst.end());
    int i = 0;
    while(i < n){
        res.push_back(lst[i]);
        i += 2;
    }
    i = 1;
    while(i < n){
        res.push_back(lst[i]);
        i += 2;
    }
    return res;
}

C:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    int n = lst.size();
    vector<int> res;
    if(n == 0){
        return res;
    }
    sort(lst.begin(), lst.end());
    int i = 0;
    while(i < n){
        res.push_back(lst[i]);
        i += 2;
    }
    i = 1;
    while(i < n){
        res.push_back(lst[i]);
        i += 2;
    }
    return res;

D:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    int n = lst.size();
    vector<int> res;
    if(n == 0){
        return res;
    }
    sort(lst.begin(), lst.end());
    int i = 0;
    while(i < n){
        res.push_back(lst[i]);
        i += 2;
    }
    i = 1;
    while(i < n){
        res.push_back(lst[i]);
        i += 2;
    }
    return res;

E:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    int n = lst.size