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
    int counter = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '<'){
            counter++;
        } else {
            counter--;
        }
        if(counter < 0){
            return false;
        }
    }
    return counter == 0;
}

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
    int counter = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '<'){
            counter++;
        } else {
            counter--;
        }
        if(counter < 0){
            return false;
        }
    }
    return counter == 0;
}

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
    int counter = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '<'){
            counter++;
        } else {
            counter--;
        }
        if(counter < 0){
            return false;
        }
    }
    return counter == 0;
}

/*
brackets is a string of '<' and '>'.
return true if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("<")
false
>>> correct_bracketing("<>")
true
>>> correct_bracketing("<<><>>")
true
>>> correct_bracketing