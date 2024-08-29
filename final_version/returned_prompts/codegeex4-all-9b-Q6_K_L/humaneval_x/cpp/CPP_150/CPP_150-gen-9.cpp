/*
A simple program which should return the value of x if n is 
a prime number and should return the value of y otherwise.

Examples:
for x_or_y(7, 34, 12) == 34
for x_or_y(15, 8, 5) == 5

*/
#include<stdio.h>
using namespace std;
int x_or_y(int n,int x,int y){

    int i;
    for (i=2;i<n;i++){
        if (n%i==0){
            return y;
        }
    }
    return x;
}

int main(){
    int x,y,n;
    cin>>n;
    cin>>x;
    cin>>y;
    cout<<x_or_y(n,x,y)<<endl;
    return 0;
}

C:
/*
A simple program which should return the value of x if n is 
a prime number and should return the value of y otherwise.

Examples:
for x_or_y(7, 34, 12) == 34
for x_or_y(15, 8, 5) == 5

*/
#include<stdio.h>
using namespace std;
int x_or_y(int n,int x,int y){

    int i;
    for (i=2;i<n;i++){
        if (n%i==0){
            return y;
        }
    }
    return x;
}

int main(){
    int x,y,n;
    cin>>n;
    cin>>x;
    cin>>y;
    cout<<x_or_y(n,x,y)<<endl;
    return 0;
}


D:
/*
A simple program which should return the value of x if n is 
a prime number and should return the value of y otherwise.

Examples:
for x_or_y(7, 34, 12) == 34
for x_or_y(15, 8, 5) == 5

*/
#include<stdio.h>
using namespace std;
int x_or_y(int n,int x,int y){

    int i;
    for (i=2;i<n;i++){
        if (n%i==0){
            return y;
        }
    }
    return x;
}

int main(){
    int x,y,n;
    cin>>n;
    cin>>x;
    cin>>y;
    cout<<x_or_y(n,x,y)<<endl;
    return 0;
}

E:
/*
A simple program which should return the value of x if n is 
a prime number and should return the value of y otherwise