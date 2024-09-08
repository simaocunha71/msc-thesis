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
    double a1=0,b1=0;
    string a2="",b2="";
    if(a.type()==typeid(string)){
        a2=boost::any_cast<string>(a);
        a1=atof(a2.c_str());
    }else{
        a1=boost::any_cast<double>(a);
    }
    if(b.type()==typeid(string)){
        b2=boost::any_cast<string>(b);
        b1=atof(b2.c_str());
    }else{
        b1=boost::any_cast<double>(b);
    }
    if(a1>b1){
        return a;
    }else if(a1<b1){
        return b;
    }else{
        return "None";
    }
}
C:
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
    double a1=0,b1=0;
    string a2="",b2="";
    if(a.type()==typeid(string)){
        a2=boost::any_cast<string>(a);
        a1=atof