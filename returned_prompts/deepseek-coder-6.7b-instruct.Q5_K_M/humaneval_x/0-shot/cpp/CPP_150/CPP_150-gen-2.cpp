    if(n == 1){
        return y;
    }
    for(int i = 2; i <= n/2; ++i){
        if(n % i == 0){
            return y;
        }
    }
    return x;
}

int main(){
    printf("%d",x_or_y(7,34,12));
    return 0;
}

*/

// C++ solution to the problem:

#include<iostream>
using namespace std;

bool isPrime(int n) {
    if (n <= 1)  return false;
    if (n <= 3)  return true;
  
    if (n%2 == 0 || n%3 == 0)
        return false;
  
    for (int i=5; i*i<=n; i=i+6)
        if (n%i == 0 || n%(i+2) == 0)
            return false;
  
    return true;
}

int x_or_y(int n,int x,int y){
    return isPrime(n) ? x : y;
}

int main(){
    cout << x_or_y(7,34,12) << endl;
    cout << x_or_y(15,8,5) << endl;
    return 0;
}

// C solution to the problem:

#include<stdio.h>

int isPrime(int n){
    if(n <= 1)
        return 0;
    for(int i = 2; i*i <= n; i++){
        if(n % i == 0)
            return 0;
    }
    return 1;
}

int x_or_y(int n,int x,int y){
    return isPrime(n) ? x : y;
}

int main(){
    printf("%d",x_or_y(7,34,12));
    return 0;
}

// Python solution to the problem:

def isPrime(n):
    if n <= 1:
        return False
