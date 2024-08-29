#include<stdio.h>
#include<math.h>
using namespace std;
int modp(int n,int p){
    int m=1;
    int p1=p;
    while(n>0){
        if(n%2==1){
            m=(m*p1)%p;
        }
        p1=(p1*p1)%p;
        n=n/2;
    }
    return m;
}
