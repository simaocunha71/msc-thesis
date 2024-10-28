
Code Review

#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>

The include order is not important, but it's often good practice to include your project specific header files first followed by standard libraries and then system headers. 
#include "myheaders.h"
#include <mylibs.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>

Prefer to use std::abs() over abs() as it avoids name collisions with other libraries.

bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

I would use a range based for loop instead of an index based loop.
for (auto const& a : numbers) {
    for (auto const& b : numbers) {
        if (a != b) {
            if (std::abs(a-b) < threshold) {
                return true;
            }
        }
    }
}
return false;

Prefer to use the standard library algorithm std::min_element() over a manual loop to find the minimum element in a vector.
float min_number = *std::min_element(numbers.begin(), numbers.end());
float max_number = *std::max_element(numbers.begin(), numbers.end());

vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
        level+=1;
        current_paren+=chr;
        }
        if (chr==')')
        {
            level-=1;
            current_paren+=chr;
            if (level==0){
                all_parens.push_back(current_paren);
                current_paren