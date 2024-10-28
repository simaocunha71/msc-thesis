
First of all, your questions should be in the same format. Here is an example of how you should format your questions:

Question: Given a positive floating point number, it can be decomposed into and integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1).

Return the decimal part of the number.

Example: truncate_number(3.5) should return 0.5.

Code:

#include<stdio.h>
#include<math.h>
using namespace std;
float truncate_number(float number){
    return number-int(number);
}

