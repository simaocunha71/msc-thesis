/*
Return length of given string
>>> strlen("")
0
>>> strlen("abc")
3
*/
#include<stdio.h>
#include<string>
using namespace std;
int strlen(string str){
    int len=0;
    for(int i=0;str[i]!='\0';i++){
        len++;
    }
    return len;
}
