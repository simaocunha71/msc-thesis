```cpp
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> bf(string planet1,string planet2){
    vector<string> res;
    string plan[8]={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    int p1=0,p2=0;
    for(int i=0;i<8;i++){
        if(planet1==plan[i]){
            p1=i;
        }
        if(planet2==plan[i]){
            p2=i;
        }
    }
    if(p1>=8||p2>=8){
        return res;
    }
    if(p1>p2){
        int temp=p1;
        p1=p2;
        p2=temp;
    }
    for(int i=p1+1;i<p2;i++){
        res.push_back(plan[i]);
    }
    return res;
}
```
