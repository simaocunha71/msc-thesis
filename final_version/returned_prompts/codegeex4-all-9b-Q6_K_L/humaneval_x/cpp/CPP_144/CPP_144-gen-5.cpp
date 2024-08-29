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
    string s1,s2,s3,s4;
    int a,b,c,d;
    a=x.find('/');
    s1=x.substr(0,a);
    s2=x.substr(a+1,x.length()-a);
    a=atoi(s1.c_str());
    b=atoi(s2.c_str());
    c=n.find('/');
    s3=n.substr(0,c);
    s4=n.substr(c+1,n.length()-c);
    c=atoi(s3.c_str());
    d=atoi(s4.c_str());
    if(a*d==b*c){
        return true;
    }
    else{
        return false;
    }
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
    string s1,s2,s3,s4;
    int a,b,c,d;
    a=x.find('/');
    s1=x.substr(0,a);
    s2=x.substr(a+1,x.length()-a);
    a=atoi(s1.c_str());
    b=atoi(s2