/*
Create a function that takes integers, floats, or strings representing
real numbers, and returns the larger variable in its given variable type.
Return "None" if the values are equal.
Note: If a real number is represented as a string, the floating point might be . or ,

compare_one(1, 2.5) ➞ 2.5
compare_one(1, "2,3") ➞ "2,3"
compare_one("5,1", "6") ➞ "6"
compare_one("1", 1) ➞ "None"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
#include<boost/any.hpp>
using namespace std;
boost::any compare_one(boost::any a,boost::any b){
    double da = 0,db = 0;
    if(a.type()==typeid(string)){
        string s = boost::any_cast<string>(a);
        da = atof(s.c_str());
    }
    else
        da = boost::any_cast<double>(a);
    if(b.type()==typeid(string)){
        string s = boost::any_cast<string>(b);
        db = atof(s.c_str());
    }
    else
        db = boost::any_cast<double>(b);
    if(da == db)
        return boost::any("None");
    else if(da > db)
        return a;
    else
        return b;
}
