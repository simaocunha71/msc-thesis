#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool monotonic(vector<float> l){
    int a=0,b=0;
    for(int i=0;i<l.size()-1;i++){
        if(l[i]<l[i+1]) a++;
        else if(l[i]>l[i+1]) b++;
    }
    if(a!=0&&b!=0) return false;
    return true;
}