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
#include<math.h>
using namespace std;
bool simplify(string x,string n){
    //split x and n into numerator and denominator
    string numerator_x, denominator_x, numerator_n, denominator_n;
    size_t pos_x = x.find('/');
    size_t pos_n = n.find('/');
    numerator_x = x.substr(0, pos_x);
    denominator_x = x.substr(pos_x + 1);
    numerator_n = n.substr(0, pos_n);
    denominator_n = n.substr(pos_n + 1);
    //convert numerator and denominator to integers
    int num_x = atoi(numerator_x.c_str());
    int den_x = atoi(denominator_x.c_str());
    int num_n = atoi(numerator_n.c_str());
    int den_n = atoi(denominator_n.c_str());
    //multiply numerator and denominator
    int num = num_x * num_n;
    int den = den_x * den_n;
    //check if the result is a whole number
    if(num % den == 0){
        return true;
    } else {
        return false;
    }

}