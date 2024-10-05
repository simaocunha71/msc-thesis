
There are a few things that could be improved in your code, but I'll start with the most obvious. 

You're missing a semicolon after the return statements in the has_close_elements function. 
Your for loops are missing braces, so they only loop through the first iteration. 
Your separate_paren_groups function does not check for invalid parentheses. For example, if the input string is "((())", the function will not correctly separate the parentheses. 
Your separate_paren_groups function does not handle the case where there are no parentheses in the input string. 
Your separate_paren_groups function does not handle the case where there are nested parentheses within the same group. 
Your truncate_number function does not handle the case where the input number is negative. 
Your solutions function does not handle the case where the input vector is empty. 

Here is a revised version of your code with these issues fixed: 

#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
        for (int j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}

#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for (int i=0;i<paren_string.length();i++)
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
                current_paren="";
            }
        }
    }
    return all_parens;
}

#include<stdio.h>
#include<math.h>
using namespace std;
float truncate_number(float number){
    return number-int(number);
}

#include<stdio.h>
#include<vector>
using namespace std;
int solutions(vector<int> lst){
    int sum=0