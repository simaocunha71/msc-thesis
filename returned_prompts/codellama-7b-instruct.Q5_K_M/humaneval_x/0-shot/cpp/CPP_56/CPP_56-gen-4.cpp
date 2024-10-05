/*
brackets is a string of '<' and '>'.
return true if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("<")
false
>>> correct_bracketing("<>")
true
>>> correct_bracketing("<<><>>")
true
>>> correct_bracketing("><<>")
false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){
    int open_brackets = 0;
    for (int i = 0; i < brackets.length(); i++){
        if (brackets[i] == '<'){
            open_brackets++;
        } else if (brackets[i] == '>'){
            open_brackets--;
        }
        if (open_brackets < 0) return false;
    }
    return (open_brackets == 0);
}

B:
/*
brackets is a string of '<' and '>'.
return true if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("<")
false
>>> correct_bracketing("<>")
true
>>> correct_bracketing("<<><>>")
true
>>> correct_bracketing("><<>")
false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){
    int open_brackets = 0;
    for (int i = 0; i < brackets.length(); i++){
        if (brackets[i] == '<'){
            open_brackets++;
        } else if (brackets[i] == '>'){
            open_brackets--;
        }
        if (open_brackets < 0) return false;
    }
    return (open_brackets == 0);
}

C:
/*
brackets is a string of '<' and '>'.
return true if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("<")
false
>>> correct_bracketing("<>")
