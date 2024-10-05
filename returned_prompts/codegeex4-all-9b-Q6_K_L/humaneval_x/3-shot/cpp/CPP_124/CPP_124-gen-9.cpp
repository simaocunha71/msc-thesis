
Your code is almost correct, but you're missing the #include <stdlib.h> for the atoi() function.  However, there's no need to use it.  The C++ string class has a method called "substr" that can be used to extract parts of the string.  It's much cleaner and easier to understand than using "atoi".  Here's a slightly modified version of your code:
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
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
    for (i=0;i<paren_string.length();i++){
        chr=paren_string[i];
        if (chr=='('){
            level+=1;
            current_paren+=chr;
        } else if (chr==')'){
            level-=1;
            current_paren+=chr;
            if (level==0){
                all_parens.push_back(current_paren);
                current_paren="";
           