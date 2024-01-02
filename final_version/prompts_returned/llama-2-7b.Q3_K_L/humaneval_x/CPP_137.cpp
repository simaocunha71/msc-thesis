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
	if(typeid(a)==typeid(b)){//same datatype
		return (a=="b"); //if yes return b, else return false
	}else{
		//convert to string
		string s_a=static_cast<const char*>(a.any());
		string s_b=static_cast<const char*>(b.any());
		int i;
		if(s_a==s_b){
			return 1; //if both strings are same return 1 otherwise 0
		}else{
			//compare strings
			for(i=0;i<strlen(s_a);++i){
				if(!tolower(s_a[i])==!tolower(s_b[i])) break; //if not same return 1 otherwise 0
			}
			return i;//if the strings are different then i will contains the last index of difference and else it will be -1
		}
	}
}