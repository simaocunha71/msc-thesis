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

    int i,j,count=0;
    char open_bracket[50],close_bracket[50];
    open_bracket[0]='<';
    close_bracket[0]='>';
    open_bracket[1]='<';
    close_bracket[1]='>';
    open_bracket[2]='<';
    close_bracket[2]='>';
    open_bracket[3]='<';
    close_bracket[3]='>';
    open_bracket[4]='<';
    close_bracket[4]='>';
    open_bracket[5]='<';
    close_bracket[5]='>';
    open_bracket[6]='<';
    close_bracket[6]='>';
    open_bracket[7]='<';
    close_bracket[7]='>';
    open_bracket[8]='<';
    close_bracket[8]='>';
    open_bracket[9]='<';
    close_bracket[9]='>';
    open_bracket[10]='<';
    close_bracket[10]='>';
    open_bracket[11]='<';
    close_bracket[11]='>';
    open_bracket[12]='<';
    close_bracket[12]='>';
    open_bracket[13]='<';
    close_bracket[13]='>';
    open_bracket[14]='<';
    close_bracket[14]='>';
    open_bracket[15]