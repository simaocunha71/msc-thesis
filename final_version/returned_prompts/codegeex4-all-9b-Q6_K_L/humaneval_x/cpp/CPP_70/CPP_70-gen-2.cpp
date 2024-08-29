#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    vector<int> res;
    sort(lst.begin(), lst.end());
    int i = 0;
    while (i < lst.size()){
        res.push_back(lst[i]);
        i += 2;
    }
    i = 1;
    while (i < lst.size()){
        res.push_back(lst[i]);
        i += 2;
    }
    return res;
}

B:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    vector<int> res;
    sort(lst.begin(), lst.end());
    for (int i = 0; i < lst.size(); i += 2){
        res.push_back(lst[i]);
    }
    for (int i = 1; i < lst.size(); i += 2){
        res.push_back(lst[i]);
    }
    return res;
}

C:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    vector<int> res;
    sort(lst.begin(), lst.end());
    int i = 0;
    int j = 1;
    while (i < lst.size() || j < lst.size()){
        if (i < lst.size()){
            res.push_back(lst[i]);
            i += 2;
        }
        if (j < lst.size()){
            res.push_back(lst[j]);
            j += 2;
        }
    }
    return res;
}

D:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    vector<int> res;
    sort(lst.begin(), lst.end());
    for (int i = 0; i < lst.size(); i++){
        if (i % 2 == 0){
            res.push_back(lst[i]);
        }
    }
    for (int i = 1; i < lst.size(); i++){
        if (i % 2 == 1){
            res.push_back(lst[i]);
        }
    }
    return res;
}

E:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    vector<int> res;
    sort(lst.begin(), lst.end());
    for (int i = 0; i < lst.size(); i++){
        if (i % 