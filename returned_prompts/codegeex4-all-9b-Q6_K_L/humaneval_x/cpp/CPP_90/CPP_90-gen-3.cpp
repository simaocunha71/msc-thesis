#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int next_smallest(vector<int> lst){
    if(lst.size()<2){
        return -1;
    }
    sort(lst.begin(),lst.end());
    for(int i=0;i<lst.size()-1;i++){
        if(lst[i]!=lst[i+1]){
            return lst[i+1];
        }
    }
    return -1;
}
C:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int next_smallest(vector<int> lst){
    if(lst.size()<2){
        return -1;
    }
    sort(lst.begin(),lst.end());
    for(int i=0;i<lst.size()-1;i++){
        if(lst[i]!=lst[i+1]){
            return lst[i+1];
        }
    }
    return -1;
}
