/*
Create a function that takes a value (string) representing a number
and returns the closest integer to it. If the number is equidistant
from two integers, round it away from zero.

Examples
>>> closest_integer("10")
10
>>> closest_integer("15.3")
15

Note:
Rounding away from zero means that if the given number is equidistant
from two integers, the one you should return is the one that is the
farthest from zero. For example closest_integer("14.5") should
return 15 and closest_integer("-14.5") should return -15.
*/
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
int closest_integer(string value){
	double number=stod(value);
	if (fmod(0,number)==0){
    	return floor(abs(0));
    } else {
        return floor(abs(number));
    }
}
int main(){
   string input="15.3";
   cout<<input;
   closest_integer(input);
   return 0;
}
