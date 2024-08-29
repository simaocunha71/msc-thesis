#include<stdio.h>
#include<vector>
using namespace std;
bool will_it_fly(vector<int> q,int w){
    int sum=0;
    int len=q.size();
    for(int i=0;i<len;i++){
        sum+=q[i];
    }
    if(sum>w){
        return false;
    }
    int i=0,j=len-1;
    while(i<j){
        if(q[i]!=q[j]){
            return false;
        }
        i++;
        j--;
    }
    return true;
}
