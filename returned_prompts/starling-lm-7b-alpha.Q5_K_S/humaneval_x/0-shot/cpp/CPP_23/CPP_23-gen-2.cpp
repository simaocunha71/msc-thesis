    int len = 0;
    for(int i = 0; i < str.length(); i++)
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
int strlen(char* str){

B:
    int len = 0;
    for(int i = 0; str[i]; i++)
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
int strlen(char* str){

C:
    int len = 0;
    for(; str[len]; len++)
        ;
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
int strlen(char* str){

D:
    int len = 0;
    for(; str[len]; len++)
        ;
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
int strlen(char* str){

E:
    int len = 0;
    while(str[len])
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
int strlen(char* str){

F:
    int len = 0;
    while(str[len])
        len++;
    return len;
}






/*
Return length of given string
>>> strlen("")
0