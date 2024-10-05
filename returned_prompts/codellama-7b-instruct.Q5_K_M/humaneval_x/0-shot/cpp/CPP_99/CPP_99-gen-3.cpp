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

    int int_value;
    int int_value_next;
    int closest_value;

    int_value = atoi(value.c_str());
    int_value_next = int_value + 1;

    closest_value = int_value;

    if(abs(closest_value - int_value) > abs(int_value_next - int_value)){
        closest_value = int_value_next;
    }

    return closest_value;
}
int main(){
    string value;
    scanf("%s", value);
    int result = closest_integer(value);
    printf("%d", result);
    return 0;
}
