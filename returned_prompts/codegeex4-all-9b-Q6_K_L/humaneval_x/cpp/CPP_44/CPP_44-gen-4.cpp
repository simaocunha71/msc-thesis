#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string s;
    if(x<base){
        s+=x;
    }else{
        s=change_base(x/base,base);
        s+=x%base;
    }
    return s;
}
B:
#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string s;
    if(x==0){
        s+=0;
    }else{
        s=change_base(x/base,base);
        s+=x%base;
    }
    return s;
}
C:
#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string s;
    if(x<base){
        s+=x;
    }else{
        s=change_base(x/base,base);
        s+=x%base;
    }
    if(x==0){
        s+=0;
    }
    return s;
}
D:
#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string s;
    if(x==0){
        s+=0;
    }else{
        s=change_base(x/base,base);
        s+=x%base;
    }
    s+=x;
    return s;
}
E:
#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string s;
    if(x==0){
        s+=0;
    }else{
        s=change_base(x/base,base);
        s+=x%base;
    }
    s+=x/base;
    return s;
}
F:
#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string s;
    if(x==0){
        s+=0;
    }else{
        s=change_base(x/base,base);
        s+=x%base;
    }
    s+=x/base;
    s+=x;
    return s;
}
G:
#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x,int base){
    string s;
    if(x==0){
        s+=0;
    }else{
        s=change_base(x/base,base);
        s+=x%base;
    }
    s+=x/base;
    s+=x%base;
    return s;
}
H:
#include<stdio.h>
#include<string>
using namespace std;
string change_base(int x