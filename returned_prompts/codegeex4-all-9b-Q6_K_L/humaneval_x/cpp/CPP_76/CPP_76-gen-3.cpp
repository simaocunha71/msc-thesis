#include<stdio.h>
#include<math.h>
using namespace std;
bool is_simple_power(int x,int n){
    int k=0;
    for(int i=1;i<=x;i++){
        if(pow(n,i)==x){
            k=1;
            break;
        }
    }
    if(k==1){
        return true;
    }
    else{
        return false;
    }
}

B:
#include<stdio.h>
#include<math.h>
using namespace std;
bool is_simple_power(int x,int n){
    int k=0;
    for(int i=0;i<=x;i++){
        if(pow(n,i)==x){
            k=1;
            break;
        }
    }
    if(k==1){
        return true;
    }
    else{
        return false;
    }
}

C:
#include<stdio.h>
#include<math.h>
using namespace std;
bool is_simple_power(int x,int n){
    int k=0;
    for(int i=0;i<x;i++){
        if(pow(n,i)==x){
            k=1;
            break;
        }
    }
    if(k==1){
        return true;
    }
    else{
        return false;
    }
}

D:
#include<stdio.h>
#include<math.h>
using namespace std;
bool is_simple_power(int x,int n){
    int k=0;
    for(int i=1;i<=x;i++){
        if(pow(n,i)==x){
            k=1;
            break;
        }
    }
    if(k==1){
        return true;
    }
    else{
        return false;
    }
}

E:
#include<stdio.h>
#include<math.h>
using namespace std;
bool is_simple_power(int x,int n){
    int k=0;
    for(int i=0;i<x;i++){
        if(pow(n,i)==x){
            k=1;
            break;
        }
    }
    if(k==1){
        return true;
    }
    else{
        return false;
    }
}

在这几个选项中，正确的答案是 A 和 D。

A 和 D 的代码都使用了 for 循环来检查从 1 到 x 的所有 n 的幂次，看是否有等于 x 的幂次。如果有，那么函数返回 true，表示 x 是一个简单的 n 的幂次。如果没有，那么函数返回 false，表示 x 不是一个简单的 n 的幂次。

B 和 C 的代码错误地使用了 for 循环从 0 开始，这可能会导致在 x