
The first function looks fine. You are using the abs() function correctly, and you are using the vector::size() function correctly to get the length of the vector. Your code is simple and easy to read.
The second function is close, but there is a bug. When you find a closing parenthesis, you check the level. If it's 0, you add the current_paren to the vector and clear it. However, you never check if the current_paren is empty before adding it to the vector. If the input string is empty, then you will add an empty string to the vector, which is not what you want.
Here's the corrected code:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
