    if(n<=2){
        return 1;
    }else{
        int a=fib(n-1);
        int b=fib(n-2);
        return a+b;
    }
}

int main(){
    printf("%d\n",fib(10));
    printf("%d\n",fib(1));
    printf("%d\n",fib(8));
    return 0;
}
































*/
#include<iostream>
using namespace std;
int fib(int n){
    if(n<=2){
        return 1;
    }else{
        int a=fib(n-1);
        int b=fib(n-2);
        return a+b;
    }
}
int main(){
    cout << fib(10) << endl;
    cout << fib(1) << endl;
    cout << fib(8) << endl;
    return 0;
}


























































































































































































































































