#include<stdio.h>
#include<vector>
using namespace std;

bool monotonic(vector<float> l){
    if(l.size()==0) return true;
    float flag = l[0];
    int i;
    for(i=1;i<l.size();i++){
        if(l[i]>flag) flag = l[i];
        else if(l[i]<flag) return false;
    }
    return true;
}

B:
#include<stdio.h>
#include<vector>
using namespace std;

bool monotonic(vector<float> l){
    if(l.size()==0) return true;
    float flag = l[0];
    int i;
    for(i=1;i<l.size();i++){
        if(l[i]<flag) flag = l[i];
        else if(l[i]>flag) return false;
    }
    return true;
}

C:
#include<stdio.h>
#include<vector>
using namespace std;

bool monotonic(vector<float> l){
    if(l.size()==0) return true;
    float flag = l[0];
    int i;
    for(i=1;i<l.size();i++){
        if(l[i]>flag) return false;
        else if(l[i]<flag) flag = l[i];
    }
    return true;
}

D:
#include<stdio.h>
#include<vector>
using namespace std;

bool monotonic(vector<float> l){
    if(l.size()==0) return true;
    float flag = l[0];
    int i;
    for(i=1;i<l.size();i++){
        if(l[i]<flag) return false;
        else if(l[i]>flag) flag = l[i];
    }
    return true;
}

E:
#include<stdio.h>
#include<vector>
using namespace std;

bool monotonic(vector<float> l){
    if(l.size()==0) return true;
    float flag = l[0];
    int i;
    for(i=1;i<l.size();i++){
        if(l[i]>flag) return false;
        else if(l[i]<flag) flag = l[i];
    }
    return false;
}

F:
#include<stdio.h>
#include<vector>
using namespace std;

bool monotonic(vector<float> l){
    if(l.size()==0) return true;
    float flag = l[0];
    int i;
    for(i=1;i<l.size();i++){
        if(l[i]<flag) return false;
        else if(l[i]>flag) flag = l[i];
    }
    return false;
}

G:
#include<stdio.h>
#include<vector>
using