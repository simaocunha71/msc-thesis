
You've got your for loops in the wrong place, and a few other little issues.
First of all, your first loop should be:
for (i = 0; i < numbers.size(); i++) {
    for (j = i + 1; j < numbers.size(); j++) {

Note that the braces should be on a new line, not on the same line as the for loop.  The same applies to your second loop.
Secondly, you should use braces for all of your loops, even if they only contain one statement.  This makes your code easier to read and maintain.
Thirdly, you need to include the header file for the abs function:
#include <cstdlib>

Lastly, your second function has a small bug.  It should be:
for (i = 0; i < paren_string.length(); i++) {
    chr = paren_string[i];

And your third function has a couple of bugs.  It should be:
if (x.length() == 3) {
    x = x.substr(2) + x.substr(0, 2);
}

And the same for the decode function:
if (x.length() == 3) {
    x = x.substr(1) + x.substr(0, 1);
}

Here's your updated code:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

#include<stdio.h>
#include<string>
#include<vector>
using namespace std;
vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    for (int i = 0; i < paren_string.length(); i++) {
        chr = paren_string[i];
        if (chr == '(')