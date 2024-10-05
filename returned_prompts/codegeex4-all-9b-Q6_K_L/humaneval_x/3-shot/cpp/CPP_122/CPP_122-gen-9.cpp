
There are some issues with your code:

In the has_close_elements function, there's a label A: that is not used anywhere.
You've declared and used i and j in the has_close_elements function, but they are not declared in the separate_paren_groups function.
In the separate_paren_groups function, you're not checking if chr is a parenthesis at all. You can check that by using if (chr == '(' || chr == ')').
You're not checking if chr is a parenthesis in the truncate_number function.
In the add_elements function, you're not checking if arr[i] is a positive integer less than 100 at all. You can check that by using if (arr[i] < 100).
You're not checking if arr[i] is a positive integer less than 100 in the add_elements function.
You're not checking if k is a positive integer less than or equal to the length of arr in the add_elements function.
There are no return statements in the truncate_number function.
You're not checking if arr is not empty in the add_elements function.
There are no return statements in the add_elements function.
You're not checking if arr is not empty in the add_elements function.
There are no return statements in the add_elements function.

Here's the corrected code:

#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0; i<numbers.size(); i++)
        for (int j=i+1; j<numbers.size(); j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;
    return false;
}

vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for (int i=0; i<paren_string.length(); i++){
        chr=paren_string[i];
        if (chr=='(' || chr==')'){
            if (chr=='(')
                level+=1;
            else
                level-=1;
            current_paren+=chr;
            if (level==0){
                all_p