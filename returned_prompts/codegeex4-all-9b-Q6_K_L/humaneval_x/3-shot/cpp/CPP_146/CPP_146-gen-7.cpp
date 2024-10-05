
Overall, your solutions are good, but there are some things that can be improved:

Your function names could be a bit more descriptive. For example, instead of has_close_elements, you could have something like has_numbers_within_threshold. This would make it clear what the function is supposed to do.
In your first function, you could use the standard library function std::abs to calculate the absolute value of the difference between the two numbers. This would make your code more readable and concise.
In your second function, you could use the standard library function std::stoi to convert the character to an integer. This would make your code more readable and concise.
In your third function, you could use the standard library function std::floor to truncate the number. This would make your code more readable and concise.
In your fourth function, you could use the standard library function std::isdigit to check if the character is a digit. This would make your code more readable and concise.

Here is the updated code:

#include<stdio.h>
#include<vector>
#include<math.h>
#include<string>
#include<ctype.h>
using namespace std;

bool has_numbers_within_threshold(vector<float> numbers, float threshold){
    int i,j;
    for (i=0;i<numbers.size();i++)
        for (j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}

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
                all_parens.push