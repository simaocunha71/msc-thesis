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
    int len = 0;
    while(str[len] != '\0'){
        len++;
    }
    return len;
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
    int len = 0;
    for(int i = 0; i < str.length(); i++){
        len++;
    }
    return len;
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
    int len = 0;
    for(char c : str){
        len++;
    }
    return len;
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
    int len = 0;
    while(str[len] != '\0'){
        len++;
    }
    return str.size();
}
E:
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
    int len = 0;
    while(str[len] != '\0'){
        len++;
    }
    return sizeof(str);
}
F:
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
    int len = 0;
    for(char c : str){
        len++;
    }
    return sizeof(c);
}
G:
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
    int len = 0;
    for(int i = 0; i < str.length(); i++){
        len++;
    }
    return sizeof(str);
}


在 C++ 中，字符串是类对象，而不是字符数组。因此，使用 `sizeof` 函数来获取字符串的大小并不适用。`sizeof` 函数返回的是对象在内存中的大小，对于字符串，这包括字符串的字符和结尾