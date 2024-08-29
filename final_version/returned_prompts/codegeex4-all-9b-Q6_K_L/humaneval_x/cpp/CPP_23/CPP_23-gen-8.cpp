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
    return str.length();
}

B:
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
    int count=0;
    for(int i=0;i<str.length();i++){
        count++;
    }
    return count;
}

C:
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
    return sizeof(str)/sizeof(str[0]);
}

D:
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
    int count=0;
    for(char c:str){
        count++;
    }
    return count;
}
