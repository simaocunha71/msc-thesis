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
#include<string>
using namespace std;
bool simplify(string x,string n){

    int numerator_x,denominator_x,numerator_n,denominator_n;
    sscanf(x.c_str(),"%d/%d",&numerator_x,&denominator_x);
    sscanf(n.c_str(),"%d/%d",&numerator_n,&denominator_n);
    int numerator=numerator_x*denominator_n;
    int denominator=denominator_x*numerator_n;
    int gcd=gcd(numerator,denominator);
    numerator=numerator/gcd;
    denominator=denominator/gcd;
    if(numerator%denominator==0) return true;
    else return false;
}
int gcd(int a,int b){
    int c;
    while(b>0){
        c=a%b;
        a=b;
        b=c;
    }
    return a;
}
int main(){
    printf("%d\n",simplify("1/5","5/1"));
    printf("%d\n",simplify("1/6","2/1"));
    printf("%d\n",simplify("7/10","10/2"));
    return 0;
}
