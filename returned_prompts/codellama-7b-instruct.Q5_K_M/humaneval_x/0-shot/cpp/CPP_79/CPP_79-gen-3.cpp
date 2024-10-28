/*
You will be given a string of binary numbers, and your task is to return the decimal
value of the binary number.

There will be an extra couple of characters "db" at the beginning and at the end of the string.
The extra characters are there to help with the format.

Examples:
binary_to_decimal("db1111db")  // returns 15
binary_to_decimal("db100000db")  // returns 32
*/
#include<stdio.h>
#include<string>
using namespace std;
int binary_to_decimal(string binary){

