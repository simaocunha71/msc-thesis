#include<stdio.h>
#include<math.h>
using namespace std;
bool iscuber(int a){
    if(a<0){
        return false;
    }
    for(int i=0;i<=a;i++){
        if(i*i*i==a){
            return true;
        }
    }
    return false;
}

B:
#include<stdio.h>
#include<math.h>
using namespace std;
bool iscuber(int a){
    if(a<0){
        return false;
    }
    for(int i=0;i<=a;i++){
        if(pow(i,3)==a){
            return true;
        }
    }
    return false;
}

C:
#include<stdio.h>
#include<math.h>
using namespace std;
bool iscuber(int a){
    if(a<0){
        return false;
    }
    for(int i=0;i<=a;i++){
        if(i*i*i==a){
            return true;
        }
        else if(i*i*i>a){
            return false;
        }
    }
    return false;
}

D:
#include<stdio.h>
#include<math.h>
using namespace std;
bool iscuber(int a){
    if(a<0){
        return false;
    }
    for(int i=0;i<=a;i++){
        if(pow(i,3)==a){
            return true;
        }
        else if(pow(i,3)>a){
            return false;
        }
    }
    return false;
}

E:
#include<stdio.h>
#include<math.h>
using namespace std;
bool iscuber(int a){
    if(a<0){
        return false;
    }
    for(int i=0;i<=a;i++){
        if(i*i*i==a){
            return true;
        }
        else if(i*i*i<a){
            return false;
        }
    }
    return false;
}

F:
#include<stdio.h>
#include<math.h>
using namespace std;
bool iscuber(int a){
    if(a<0){
        return false;
    }
    for(int i=0;i<=a;i++){
        if(pow(i,3)==a){
            return true;
        }
        else if(pow(i,3)<a){
            return false;
        }
    }
    return false;
}

正确答案是 B 和 D。

B 和 D 的代码都使用了 pow 函数来计算 i 的三次方，这与题目描述相符。此外，B 和 D 的代码在 i 的三次方大于 a 时直接返回 false，避免了不必要的计算，这是更优的解法。

A