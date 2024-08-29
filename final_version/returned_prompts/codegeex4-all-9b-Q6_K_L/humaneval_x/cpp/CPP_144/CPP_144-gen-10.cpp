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
#include<sstream>
using namespace std;
bool simplify(string x,string n){
    int numerator_x,denominator_x,numerator_n,denominator_n;
    stringstream ss1(x);
    ss1>>numerator_x>>denominator_x;
    stringstream ss2(n);
    ss2>>numerator_n>>denominator_n;
    if(numerator_x*denominator_n == denominator_x* numerator_n) return true;
    if(numerator_x*denominator_n % denominator_x* numerator_n == 0) return true;
    else return false;
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
#include<sstream>
using namespace std;
bool simplify(string x,string n){
    int numerator_x,denominator_x,numerator_n,denominator_n;
    stringstream ss1(x);
    ss1>>numerator_x>>denominator_x;
    stringstream ss2(n);
    ss2>>numerator_n>>denominator_n;
    if(numerator_x*denominator_n == denominator_x* numerator_n) return true;
    if(numerator_x*denominator_n % denominator_x* numerator