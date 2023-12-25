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
    int spaces = 0;
    for (int i=text.length();i>=0;i--)
        if (text[i]==' ') spaces++;
    else {
        if (spaces==2 || spaces==3 ) text[i-1]='-';
        spaces--;
    }
    if(spaces>0){
        for (int i=text.length();i>=0;i--)
            if ((!spaces && text[i-1]==' ')||!text[i].isalnum()) {
                text[i-1]=text[i];}else{spaces++;}
    }
return text;
}
int main(){
    string s="";
    int i=0,j=0,k,l=0;
    char ch=' ';
    while(true){s+=ch;if((++j)==i) break;}
for (int j=0;j<i;j++) if((int)ch!=-1 && ((char)j>=57&&(char)j<=90)) {k+=(int)(j-48);l++;}
s+=l/2+l%2==1?" ":"";
    system("clear");
    puts(fix_spaces(s));puts("");
return 0;
}
