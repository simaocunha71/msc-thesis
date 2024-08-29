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
    try{
        double aa=boost::any_cast<double>(a);
        double bb=boost::any_cast<double>(b);
        if(aa==bb) return "None";
        else if(aa>bb) return a;
        else return b;
    }
    catch(boost::bad_any_cast& e){
        try{
            string aa=boost::any_cast<string>(a);
            string bb=boost::any_cast<string>(b);
            if(aa==bb) return "None";
            else if(aa>bb) return a;
            else return b;
        }
        catch(boost::bad_any_cast& e){
            return "None";
        }
    }
} 
int main(){
    cout<<compare_one(1, 2.5)<<endl;
    cout<<compare_one(1, "2,3")<<endl;
    cout<<compare_one("5,1", "6")<<endl;
    cout<<compare_one("1", 1)<<endl;
}

