/*
Your task is to implement a function that will simplify the expression
x * n. The function returns true if x * n evaluates to a whole number and false
otherwise. Both x and n, are string representation of a fraction, and have the following format,
<numerator>/<denominator> where both numerator and denominator are positive whole numbers.

You can assume that x, and n are valid fractions, and do not have zero as denominator.

simplify("1/5", "5/1") = true
simplify("1/6", "2/1") = false
simplify("7/10", "10/2") = false
*/
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
bool simplify(string x,string n){
    int numx=0,numn=0,denx=0,denn=0,flag=0;
    for(int i=0;i<x.length();i++){
        if(x[i]=='/'){
            flag=1;
            continue;
        }
        if(flag==0){
            numx=numx*10+x[i]-'0';
        }
        else{
            denx=denx*10+x[i]-'0';
        }
    }
    flag=0;
    for(int i=0;i<n.length();i++){
        if(n[i]=='/'){
            flag=1;
            continue;
        }
        if(flag==0){
            numn=numn*10+n[i]-'0';
        }
        else{
            denn=denn*10+n[i]-'0';
        }
    }
    if(numx*numn%denx*denn==0){
        return true;
    }
    return false;
}

B:
/*
Your task is to implement a function that will simplify the expression
x * n. The function returns true if x * n evaluates to a whole number and false
otherwise. Both x and n, are string representation of a fraction, and have the following format,
<numerator>/<denominator> where both numerator and denominator are positive whole numbers.

You can assume that x, and n are valid fractions, and do not have zero as denominator.

simplify("1/5", "5/1") = true
simplify("1/6", "2/1") = false
simplify("7/10", "10/2") = false
*/
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
bool simplify(string x,string n){
    int