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
    int len = brackets.size();
    int num_left = 0;
    int num_right = 0;
    for(int i=0; i<len; i++){
        if(brackets[i] == '<'){
            num_left++;
        }
        else if(brackets[i] == '>'){
            num_right++;
            if(num_right > num_left){
                return false;
            }
        }
    }
    if(num_right == num_left){
        return true;
    }
    else{
        return false;
    }
}

C:
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
    int len = brackets.size();
    int num_left = 0;
    int num_right = 0;
    for(int i=0; i<len; i++){
        if(brackets[i] == '<'){
            num_left++;
        }
        else if(brackets[i] == '>'){
            num_right++;
            if(num_right > num_left){
                return false;
            }
        }
    }
    if(num_right == num_left){
        return true;
    }
    else{
        return false;
    }
}
