The function `numerical_letter_grade` takes a vector of floats as input and returns a vector of strings. It iterates over each grade in the input vector and determines the corresponding letter grade using a series of if-else statements.

Here's the code:

```cpp
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

vector<string> numerical_letter_grade(vector<float> grades) {
    vector<string> letter_grades;
    for(auto &grade:grades){
        if(grade>=4.0) letter_grades.push_back("A+");
        else if(grade>3.7) letter_grades.push_back("A");
        else if(grade>3.3) letter_grades.push_back("A-");
        else if(grade>3.0) letter_grades.push_back("B+");
        else if(grade>2.7) letter_grades.push_back