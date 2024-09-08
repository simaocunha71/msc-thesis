```c++
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
bool monotonic(vector<float> l){
    float s=0;
    int len=l.size();
    if(len==0) return false;
    if(len==1) return true;
    for(int i=0;i<len-1;i++){
        if(l[i]>l[i+1]) s-=1;
        if(l[i]<l[i+1]) s+=1;
    }
    if(s==len-1 || s==-len+1) return true;
    return false;
}
```
B:
```c++
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
bool monotonic(vector<float> l){
    float s=0;
    int len=l.size();
    if(len==0) return false;
    if(len==1) return true;
    for(int i=0;i<len-1;i++){
        if(l[i]>l[i+1]) s+=1;
        if(l[i]<l[i+1]) s-=1;
    }
    if(s==len-1 || s==-len+1) return true;
    return false;
}
```
C:
```c++
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
bool monotonic(vector<float> l){
    float s=0;
    int len=l.size();
    if(len==0) return false;
    if(len==1) return true;
    for(int i=0;i<len-1;i++){
        if(l[i]>=l[i+1]) s+=1;
        if(l[i]<=l[i+1]) s-=1;
    }
    if(s==len-1 || s==-len+1) return true;
    return false;
}
```
D:
```c++
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
bool monotonic(vector<float> l){
    float s=0;
    int len=l.size();
    if(len==0) return false;
    if(len==1) return true;
    for(int i=0;i<len-1;i++){
        if(l[i]==l[i+1]) s+=1;
        if(l[i]!=l[i+1]) s-=1;
    }
    if(s==len-1 || s==-len+1) return true;
    return false;
}
```
E:
```c++
#include<stdio.h>
#include<math.h>
