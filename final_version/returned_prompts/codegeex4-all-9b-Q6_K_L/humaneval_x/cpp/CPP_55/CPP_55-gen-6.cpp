/*#include <iostream>
#include <vector>
using namespace std;
int fib(int n){
    vector<int> fibo(n+1,0);
    fibo[1]=1;
    for(int i=2;i<=n;i++){
        fibo[i]=fibo[i-1]+fibo[i-2];
    }
    return fibo[n];
}
*/
B:
#include <iostream>
#include <vector>
using namespace std;
int fib(int n){
    if(n==0) return 0;
    if(n==1) return 1;
    return fib(n-1)+fib(n-2);
}

C:
#include <iostream>
using namespace std;
int fib(int n){
    int fibo[n+1];
    fibo[0]=0;
    fibo[1]=1;
    for(int i=2;i<=n;i++){
        fibo[i]=fibo[i-1]+fibo[i-2];
    }
    return fibo[n];
}
D:
#include <iostream>
using namespace std;
int fib(int n){
    int fibo[n+1];
    fibo[0]=0;
    fibo[1]=1;
    for(int i=2;i<=n;i++){
        fibo[i]=fibo[i-1]+fibo[i-2];
    }
    return fibo[n];
}

E:
#include <iostream>
using namespace std;
int fib(int n){
    int fibo[100];
    fibo[0]=0;
    fibo[1]=1;
    for(int i=2;i<=n;i++){
        fibo[i]=fibo[i-1]+fibo[i-2];
    }
    return fibo[n];
}
F:
#include <iostream>
using namespace std;
int fib(int n){
    int fibo[10000000000];
    fibo[0]=0;
    fibo[1]=1;
    for(int i=2;i<=n;i++){
        fibo[i]=fibo[i-1]+fibo[i-2];
    }
    return fibo[n];
}
G:
#include <iostream>
#include <vector>
using namespace std;
int fib(int n){
    if(n==0) return 0;
    if(n==1) return 1;
    return fib(n-1)+fib(n-2);
}
H:
#include <iostream>
using namespace std;
int fib(int n){
    int fibo[10000000000];
   