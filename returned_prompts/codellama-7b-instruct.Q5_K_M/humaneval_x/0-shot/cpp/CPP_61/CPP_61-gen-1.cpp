/*
brackets is a string of '(' and ')'.
return true if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("(")
false
>>> correct_bracketing("()")
true
>>> correct_bracketing("(()())")
true
>>> correct_bracketing(")(()")
false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){

    int i = 0;
    while (brackets[i] != '\0'){
        if (brackets[i] == '('){
            // if we find an open bracket,
            // we need to find a close bracket
            // and make sure they match
            int j = i + 1;
            while (brackets[j] != '\0'){
                if (brackets[j] == ')'){
                    // we have a match
                    i = j;
                    break;
                }
                j++;
            }
            if (brackets[j] == '\0'){
                // we didn't find a match
                return false;
            }
        }
        i++;
    }
    return true;
}
