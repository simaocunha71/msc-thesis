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
#include<math.h>
#include<string>
#include<algorithm>
#include<boost/any.hpp>
using namespace std;
double myatof(string s){
    string::iterator end = remove(s.begin(), s.end(), ',');
    s.erase(end, s.end());
    return atof(s.c_str());
}
boost::any compare_one(boost::any a,boost::any b){
    boost::any c;
    double d1,d2;
    string s1,s2;
    if(a.type()==typeid(int)){
        d1=boost::any_cast<int>(a);
        d2=boost::any_cast<int>(b);
    }
    else if(a.type()==typeid(double)){
        d1=boost::any_cast<double>(a);
        d2=boost::any_cast<double>(b);
    }
    else if(a.type()==typeid(string)){
        s1=boost::any_cast<string>(a);
        s2=boost::any_cast<string>(b);
        d1=myatof(s1);
        d2=myatof(s2);
    }
    if(d1==d2){
        c=string("None");
    }
    else{
        if(d1>d2){
            if(a.type()==typeid(int)){
                c=d1;
            }
            else if(a.type()==typeid(double)){
                c=d1;
            }
            else if(a.type()==typeid(string)){
                c=s1;
            }
        }
        else{
            if(a.type()==typeid(int)){
                c=d2;
            }
            else if(a.type()==typeid(double)){
                c=d2;
            }
            else if(a.type()==typeid(string)){
                c=s2;
            }
        }
    }
    return c;
}
