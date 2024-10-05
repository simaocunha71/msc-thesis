#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){

    int open = 0;
    int len = brackets.length();
    for(int i=0;i<len;i++){
        if(brackets[i]=='<'){
            open++;
        }else if(brackets[i]=='>'){
            open--;
            if(open<0) return false;
        }
    }
    return open==0;
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

    int open = 0;
    int len = brackets.length();
    for(int i=0;i<len;i++){
        if(brackets[i]=='<'){
            open++;
        }else if(brackets[i]=='>'){
            open--;
            if(open<0) return false;
        }
    }
    return open==0;
}



























/*
brackets is a string of '<' and '>'.
return true if every opening br