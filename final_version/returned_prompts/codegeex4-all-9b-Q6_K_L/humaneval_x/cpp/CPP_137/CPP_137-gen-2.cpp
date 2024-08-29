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
    if (a.type()==typeid(string)){
        string str_a = boost::any_cast<string>(a);
        if (str_a.find(',') != string::npos){
            replace(str_a.begin(),str_a.end(),',','.');
        }
        double d_a = stod(str_a);
        if (b.type()==typeid(string)){
            string str_b = boost::any_cast<string>(b);
            if (str_b.find(',') != string::npos){
                replace(str_b.begin(),str_b.end(),',','.');
            }
            double d_b = stod(str_b);
            if (d_a==d_b){
                return boost::any("None");
            }
            else if (d_a>d_b){
                return boost::any(d_a);
            }
            else{
                return boost::any(d_b);
            }
        }
        else if (b.type()==typeid(double)){
            double d_b = boost::any_cast<double>(b);
            if (d_a==d_b){
                return boost::any("None");
            }
            else if (d_a>d_b){
                return boost::any(d_a);
            }
            else{
                return boost::any(d_b);
            }
        }
        else if (b.type()==typeid(int)){
            int i_b = boost::any_cast<int>(b);
            double d_b = i_b;
            if (d_a==d_b){
                return boost::any("None");
            }
            else if (d_a>d_b){
                return boost::any(d_a);
            }
            else{
                return boost::any(d_b);
            }
        }
    }
    else if (a.type()==typeid(double)){
        double d_a = boost::any_cast<double>(a);
