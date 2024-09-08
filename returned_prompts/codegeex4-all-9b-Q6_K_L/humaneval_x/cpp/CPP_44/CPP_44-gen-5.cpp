#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string ret;
    int y=x;
    while(y){
        int t=y%base;
        if(t<10)
            ret+=t+'0';
        else
            ret+=t-10+'A';
        y=y/base;
    }
    if(ret.size()==0)
        ret+='0';
    reverse(ret.begin(),ret.end());
    return ret;
}
B:
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string ret;
    int y=x;
    while(y){
        int t=y%base;
        if(t<10)
            ret+=t+'0';
        else
            ret+='A'+t-10;
        y=y/base;
    }
    if(ret.size()==0)
        ret+='0';
    reverse(ret.begin(),ret.end());
    return ret;
}
C:
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string ret;
    int y=x;
    while(y){
        int t=y%base;
        if(t<10)
            ret+=t+'0';
        else
            ret+=t-10+'A';
        y=y/base;
    }
    if(ret.size()==0)
        ret+='0';
    reverse(ret.begin(),ret.end());
    return ret;
}
D:
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string ret;
    int y=x;
    while(y){
        int t=y%base;
        if(t<10)
            ret+=t+'0';
        else
            ret+=t+'A';
        y=y/base;
    }
    if(ret.size()==0)
        ret+='0';
    reverse(ret.begin(),ret.end());
    return ret;
}
E:
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string ret;
    int y=x;
    while(y){
        int t=y%base;
        if(t<10)
            ret+=t+'0';
        else
            ret+=t+'A';
        y=y/base;
    }
    if(ret.size()==0)
        ret+='0';
    reverse(ret.begin(),ret.end());
    return ret;
}
F:
#include