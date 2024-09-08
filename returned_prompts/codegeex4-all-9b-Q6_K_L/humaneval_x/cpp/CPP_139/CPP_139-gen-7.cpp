#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    if(n==1) return 1;
    return n*special_factorial(n-1)*special_factorial(n-2);
}

B:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    if(n==1) return 1;
    if(n==2) return 2;
    return n*special_factorial(n-1)*special_factorial(n-2);
}

C:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    if(n==1) return 1;
    if(n==0) return 1;
    return n*special_factorial(n-1)*special_factorial(n-2);
}

D:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    if(n==0) return 1;
    return n*special_factorial(n-1)*special_factorial(n-2);
}

E:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    if(n==1) return 1;
    return n*special_factorial(n-1);
}

F:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    if(n==0) return 1;
    return n*special_factorial(n-1);
}

G:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    if(n==1) return 1;
    return n*special_factorial(n-1)*special_factorial(n-3);
}

H:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    if(n==1) return 1;
    return n*special_factorial(n-1)*special_factorial(n-1);
}

I:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    if(n==1) return 1;
    return n*special_factorial(n-1)*special_factorial(n-2)*special_factorial(n-3);
}

J:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    if(n==1) return 1;
    if(n==2) return 2;
    return n*special_factorial(n-1)*special_factorial(n-3);
}

K:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    if(n