/*
Input to this function is a string representing mathematical expressions in a special ASCII format.
Your task is to parse this string and return vector of integers corresponding to numbers in the expression.

Here is a legend:
"+" - addition
"-" - subtraction
"*" - multiplication
"/" - division
"(" - opening bracket
")" - closing bracket

>>> parse_math("1 + 2 * 3")
{1, 2, 3, 1, 3, 2}
>>> parse_math("1 + (2 * 3)")
{1, 2, 3, 1, 3, 2}
>>> parse_math("(1 + 2) * 3")
{1, 2, 3, 3}
>>> parse_math("1 + 2 * (3 - 1)")
{1, 2, 3, 1, 2, 3}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector