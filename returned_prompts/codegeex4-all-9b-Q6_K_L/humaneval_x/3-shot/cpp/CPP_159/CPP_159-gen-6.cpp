    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

This is a good start but not a complete implementation.  The function should be a complete function and have a return value.  It should have a comment describing its purpose, its parameters and its return value.  It should also have error checking.  For example, if the vector is empty the function will return false but that is incorrect.  It should return true if the vector has less than 2 elements.  If the threshold is negative the function will return true for all pairs of numbers.  It should return false for a threshold of zero and false for all pairs of numbers if the threshold is greater than zero.
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
    if (threshold < 0)
        return true;
    if (numbers.size() < 2)
        return true;
    for (int i=0;i<numbers.size();i++)
        for (int j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j]) < threshold)
                return true;
    return false;
}

#include<stdio.h>
#include<vector>
#include<string