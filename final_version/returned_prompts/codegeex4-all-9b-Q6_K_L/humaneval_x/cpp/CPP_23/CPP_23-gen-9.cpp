#include<stdio.h>
#include<string>
using namespace std;
int strlen(string str){
    int len = str.length();
    return len;
}

B:
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
#include<stdio.h>
#include<string>
using namespace std;
int strlen(string str){
    int len = str.size();
    return len;
}