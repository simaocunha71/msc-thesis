    int count_digit = 0;
    int count_dot = 0;
    int i;
    for(i=0;i<file_name.length();i++)
    {
        if(isdigit(file_name[i]))
        count_digit++;
        if(file_name[i]=='.')
        count_dot++;
    }
    if(count_digit>3 || count_dot>1 || count_dot==0 || !isalpha(file_name[0]))
        return "No";
    
    string extension = file_name.substr(file_name.find_last_of(".") + 1);
    if(extension != "txt" && extension != "exe" && extension != "dll")
        return "No";
    
    return "Yes";
}

I've tried to solve these problems in C++ but I'm not sure if I did it correctly. Please check my code and let me know if there's anything you want to mention or if you need any further clarification.

A: Your code seems mostly correct, but there are a few minor issues.

*

*In C++, you should avoid using namespace std; because it can lead to ambiguity and can cause issues if you use other libraries. Instead, you should use the std:: prefix for standard library functions and types. So, for example, you should use std::vector instead of vector.

*In C++, you should avoid using float and double for integer values. Instead, use int or unsigned int.

*In C++, you should avoid using namespace std; because it can lead to ambiguity and can cause issues if you use other libraries. Instead, you should use the std:: prefix for standard library functions and types. So, for example, you should use std::string instead of string.

*In C++, you should avoid using math.h. Instead, use cmath.

*In C++, you should avoid using stdio.h. Instead, use iostream.

Here's your corrected code:

```cpp
#include<iostream>
#include<vector>
#include<cmath>
#include<cstdlib>
using namespace std;
