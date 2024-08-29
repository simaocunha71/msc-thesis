#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    vector<int> out={};
    int i=0;
    while(lst.size()>0){
        out.push_back(lst[0]);
        lst.erase(lst.begin());
        sort(lst.begin(), lst.end());
        if(lst.size()>0)
            out.push_back(lst[lst.size()-1]);
        lst.pop_back();
        sort(lst.begin(), lst.end());
    }
    return out;
}

B:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    vector<int> out={};
    while(lst.size()>0){
        sort(lst.begin(), lst.end());
        out.push_back(lst[0]);
        lst.erase(lst.begin());
        if(lst.size()>0)
            out.push_back(lst[lst.size()-1]);
        lst.pop_back();
    }
    return out;
}

C:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    vector<int> out={};
    while(lst.size()>0){
        if(lst.size()%2==0)
            out.push_back(lst[0]);
        else
            out.push_back(lst[lst.size()-1]);
        lst.erase(lst.begin());
        sort(lst.begin(), lst.end());
    }
    return out;
}

D:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    vector<int> out={};
    while(lst.size()>0){
        out.push_back(lst[0]);
        lst.erase(lst.begin());
        if(lst.size()>0)
            out.push_back(lst[lst.size()-1]);
        lst.pop_back();
        sort(lst.begin(), lst.end());
    }
    return out;
}

E:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
    vector<int> out={};
    int i=0;
    while(lst.size()>0){
        if(i%2==0)
            out.push_back(lst[0]);
        else
            out.push_back(lst[lst.size()-1]);
        lst.erase(lst.begin());
        sort(lst.begin(), lst.end());
        i++;
    }
    return out;
}

F:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
