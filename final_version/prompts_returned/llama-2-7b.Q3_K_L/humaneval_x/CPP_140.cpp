/*
Given a string text, replace all spaces in it with underscores, 
and if a string has more than 2 consecutive spaces, 
then replace all consecutive spaces with - 

fix_spaces("Example") == "Example"
fix_spaces("Example 1") == "Example_1"
fix_spaces(" Example 2") == "_Example_2"
fix_spaces(" Example   3") == "_Example-3"
*/
#include<stdio.h>
#include<string>
using namespace std;
string fix_spaces(string text){
    int len = strlen(text);
    for (int i=0 ; i<=len - 1 ; i++){
        if(text[i]==' ') {
            text.replace(i,1,'_');
            i++;
        }
    }
    return text;
}