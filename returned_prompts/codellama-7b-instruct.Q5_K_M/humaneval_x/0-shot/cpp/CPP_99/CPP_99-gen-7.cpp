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

    int n;
    stringstream ss(value);
    ss >> n;

    double f = n - floor(n);
    if (f <= 0.5) return n;
    else return n + 1;
}

B:
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

    double n = atof(value.c_str());
    return (int) (n > 0 ? ceil(n) : floor(n));
}

C:
/*
Create a function that takes a value (string) representing a number
and returns the closest integer to it. If the number is