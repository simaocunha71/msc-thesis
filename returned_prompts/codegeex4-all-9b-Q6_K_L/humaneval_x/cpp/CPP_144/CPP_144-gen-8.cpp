#include<stdio.h>
#include<string>
using namespace std;
bool simplify(string x,string n){
    int x1,x2,n1,n2;
    sscanf(x.c_str(),"%d/%d",&x1,&x2);
    sscanf(n.c_str(),"%d/%d",&n1,&n2);
    int x3=x1*n2,x4=x2*n1;
    if(x3%x4==0)
    return true;
    return false;
}