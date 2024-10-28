    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

This function is fine, but there are a few things that could be improved:

Your function is not efficient. You are looping through all pairs of elements. This can be optimized by sorting the array first and then only comparing adjacent elements.
Your function is not very clear. You should add comments explaining what each part of the function does.
Your function is not very robust. It does not handle the case where the input vector is empty.

Here is an improved version of the function:
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

    // Sort the vector
   