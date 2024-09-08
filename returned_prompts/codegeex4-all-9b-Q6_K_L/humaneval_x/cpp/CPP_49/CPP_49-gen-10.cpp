#include<stdio.h>
#include<math.h>
using namespace std;
int modp(int n,int p){
    int res=1;
    while(n>0){
        if(n%2==1){
            res=res*p;
            res=res%p;
        }
        n=n/2;
        p=p*p;
        p=p%p;
    }
    return res;
}

B:
#include<stdio.h>
using namespace std;
int modp(int n,int p){
    if(n==1)
        return p;
    else if(n==0)
        return 1;
    else
        return modp(n/2,p)*modp(n/2,p)%p;
    return 0;
}

C:
#include<stdio.h>
using namespace std;
int modp(int n,int p){
    if(n==1)
        return p;
    else if(n==0)
        return 1;
    else
        return modp(n/2,p)*modp(n/2,p)%p;
    return 0;
}

D:
#include<stdio.h>
using namespace std;
int modp(int n,int p){
    int res=1;
    while(n>0){
        if(n%2==1){
            res=res*p;
            res=res%p;
        }
        n=n/2;
        p=p*p;
        p=p%p;
    }
    return res;
}

E:
#include<stdio.h>
using namespace std;
int modp(int n,int p){
    if(n==1)
        return p;
    else if(n==0)
        return 1;
    else
        return modp(n/2,p)*modp(n/2,p)%p;
    return 0;
}

F:
#include<stdio.h>
using namespace std;
int modp(int n,int p){
    int res=1;
    while(n>0){
        if(n%2==1){
            res=res*p;
            res=res%p;
        }
        n=n/2;
        p=p*p;
        p=p%p;
    }
    return res;
}

G:
#include<stdio.h>
using namespace std;
int modp(int n,int p){
    int res=1;
    while(n>0){
        if(n%2==1){
            res=res*p;
            res=res%p;
        }
        n=n/2;
        p=p*p;
        p=p%p;
    }
    return res;
}

H:
#include<stdio.h>
#include<math.h>
using namespace std;
int