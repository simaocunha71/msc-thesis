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
    int i = 0;
    for(i = 0; i < value.size(); i++){
        if(value[i] == '.'){
            break;
        }
    }
    int j = 0;
    for(j = i + 1; j < value.size(); j++){
        if(value[j] == '.'){
            break;
        }
    }
    value[i] = '\0';
    value[j] = '\0';
    int num = atoi(value.c_str());
    int rem = abs(num%2);
    if(rem == 0){
        return num - rem;
    }
    else{
        return num + (2 - rem);
    }
}
int main(){
    string value;
    cin>>value;
    int num = closest_integer(value);
    cout<<num<<endl;
}
