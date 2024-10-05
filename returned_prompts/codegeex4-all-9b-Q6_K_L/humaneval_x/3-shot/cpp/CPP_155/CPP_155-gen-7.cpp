
This is a pretty decent start, but there are some improvements to be made. Here are some comments on your code:

Naming
Your variable names are generally descriptive, which is good. However, some of them are a bit long, and could be shortened. For example, in the even_odd_count function, the variable name num_s is not descriptive of the type of data it holds. A better name would be num_str.

Code Style
You have a consistent indentation style, which is good. However, you could use a more consistent line length. Most code style guides recommend a line length of 80 characters or less.

Error Checking
In the even_odd_count function, you don't check if the input number is negative. This could lead to incorrect results. You should add an if statement to check if the input number is negative, and handle it appropriately.

Return Statement
In the has_close_elements function, your return statement is inside a loop. This is not a good practice, as it will cause the function to return as soon as it finds two numbers that are closer than the threshold, even if there are other pairs of numbers that are closer. You should move the return statement outside of the loop.

Here is a revised version of your code with these comments taken into account:

/*
Check if in given vector of numbers, are any two numbers closer to each other than
given threshold.
>>> has_close_elements({1.0, 2.0, 3.0}, 0.5)
false
>>> has_close_elements({1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
true
*/
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){

    for (int i=0;i<numbers.size();i++){
        for (int j=i+