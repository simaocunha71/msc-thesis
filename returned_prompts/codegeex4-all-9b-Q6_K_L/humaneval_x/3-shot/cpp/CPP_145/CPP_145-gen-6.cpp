
You're on the right track, but you need to work on the algorithm. Let's start with the first function.
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
    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

The above solution will work, but you're checking all pairs of numbers in the vector, and this is not necessary. You're comparing each number in the vector with every other number. Instead, you should only compare each number with its immediate neighbor. This can be done by modifying your outer loop. You can also put the return false statement outside the inner loop. Here's the modified code:
bool has_close_elements(vector<float> numbers, float threshold){
    int i;
    
    for (i=0;i<numbers.size()-1;i++)
    if (abs(numbers[i]-numbers[i+1])<threshold)
    return true;

    return false;
}

The next question involves using the STL library and string manipulation:
/*
Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
separate those group into separate strings and return the vector of those.
Separate groups are balanced (each open brace is properly closed) and not nested within each other
Ignore any spaces in the input string.
>>> separate_paren_groups("( ) (( )) (( )( ))")
{"()", "(())", "(()())"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
   