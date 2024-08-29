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
    int num1 = 0, den1 = 0, num2 = 0, den2 = 0, num = 0, den = 0;
    for(int i = 0; i < x.length(); i++) {
        if(x[i] == '/') {
            num1 = atoi(x.substr(0, i).c_str());
            den1 = atoi(x.substr(i+1).c_str());
            break;
        }
    }
    for(int i = 0; i < n.length(); i++) {
        if(n[i] == '/') {
            num2 = atoi(n.substr(0, i).c_str());
            den2 = atoi(n.substr(i+1).c_str());
            break;
        }
    }
    num = num1 * num2;
    den = den1 * den2;
    if(num % den == 0) {
        return true;
    } else {
        return false;
    }
}