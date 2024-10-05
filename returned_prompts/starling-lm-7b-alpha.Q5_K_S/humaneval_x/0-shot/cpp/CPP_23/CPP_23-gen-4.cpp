    int len=0;
    for(int i=0;i<str.length();i++)
        len++;
    return len;
}




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
int strlen(char str[]){

B:
    int len=0;
    for(int i=0;str[i]!='\0';i++)
        len++;
    return len;
}




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
int strlen(const char *str){

C:
    int len=0;
    for(int i=0;str[i]!='\0';i++)
        len++;
    return len;
}




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
int strlen(char *str){

D:
    int len=0;
    for(int i=0;str[i]!='\0';i++)
        len++;
    return len;
}



















































































































































































