    if(x==0){
        return false;
    }
    else if(x==1){
        return true;
    }
    else if(x%n==0){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    int x,n;
    while(scanf("%d%d",&x,&n)!=EOF){
        if(is_simple_power(x,n)){
            printf("true\n");
        }
        else{
            printf("false\n");
        }
    }
    return 0;
}


Ans:
/*
Your task is to write a function that returns true if a number x is a simple
power of n and false in other cases.
x is a simple power of n if n**int=x
For example:
is_simple_power(1, 4) => true
is_simple_power(2, 2) => true
is_simple_power(8, 2) => true
is_simple_power(3, 2) => false
is_simple_power(3, 1) => false
is_simple_power(5, 3) => false
*/
#include<stdio.h>
#include<math.h>
using namespace std;
bool is_simple_power(int x,int n){
    if(x==0){
        return false;
    }
    else if(x==1){
        return true;
    }
    else if(x%n==0){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    int x,n;
    while(scanf("%d%d",&x,&n)!=EOF){
        if(is_simple_power(x,n)){
            printf("true\n");
        }
        else{
            printf("false\n");
        }
    }
    return 0;
}
















