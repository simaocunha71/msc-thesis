
First of all, I don't know C++, so I'll be giving C and C++ style feedback.
Second, your code looks like it was written in C and then converted to C++ using a utility, which means you are missing out on C++'s strengths (like the STL).

#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<math.h>
using namespace std;

This is not a problem, but it's not the best style. You should include the headers you use in the same order as you use them in the file (after all, it's easier to find the header you're using). And you shouldn't use the std:: prefix when including the headers.

bool has_close_elements(vector<float> numbers, float threshold){

This is good. However, you should use the const qualifier when you don't plan on modifying the parameter. This tells the compiler to optimize the function a bit more and also tells the person reading the code that the function doesn't modify the parameter.

int i,j;

This is not a problem, but you should use the auto keyword when the type of the variable can be inferred from the initializer. This makes your code a bit cleaner and reduces the risk of making a typo. Also, you should use braces around the for loop variables.

for (i=0;i<numbers.size();i++)
for (j=i+1;j<numbers.size();j++)

This is good, but you can make it more efficient by starting j at i+1, which removes the need for the if statement.

if (abs(numbers[i]-numbers[j])<threshold)
return true;

This is good. However, you should use the fabs function instead of the abs function for floating point numbers.

return false;

This is good. However, you should use the std::vector::empty function instead of comparing the size to zero.

vector<string> separate_paren_groups(string paren_string){

This is good. However, you should use the const qualifier when you don't plan on modifying the parameter. This tells the compiler to optimize the function a bit more and also tells the person reading the code