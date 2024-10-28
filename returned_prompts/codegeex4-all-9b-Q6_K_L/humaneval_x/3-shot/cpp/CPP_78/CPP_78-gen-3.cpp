
Your first function is a good start, but it has an off-by-one error in the inner loop's terminating condition. It should be j < numbers.size(), not j < numbers.size() - 1.
Your second function is good. However, you should check if level is negative before adding a closing parenthesis to current_paren. This will prevent a potential segmentation fault if the input string is not balanced.
Your third function is good. However, it is more idiomatic to use fmodf() or fmod() instead of int() for floating-point truncation.
Your fourth function is good. However, you should use tolower() to make the function case-insensitive.

Here is the corrected code:
#include<stdio.h>
#include<vector>
#include<math.h>
#include<algorithm>
#include<string>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    int i, j;
    for (i = 0; i < numbers.size(); i++)
        for (j = i + 1; j < numbers.size(); j++)
            if (abs(numbers[i] - numbers[j]) < threshold)
                return true;
    return false;
}
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i;
    for (i = 0; i < paren_string.length(); i++){
        chr = paren_string[i];
        if (chr == '('){
            level += 1;
            current_paren += chr;
        }
        if (chr == ')'){
            if (level > 0){
                level -= 1;
                current_paren += chr;
                if (level == 0){
                    all_parens.push_back(current_paren);
                    current_paren = "";
                }
            }
        }
    }
    return all_parens;
}
float truncate_number(float number){
    return fmodf(number, 1.0f);
}
int hex_key(string num){
    int i;
    int count = 0;
    string primes = "2357BDF";
    for (i = 0; i