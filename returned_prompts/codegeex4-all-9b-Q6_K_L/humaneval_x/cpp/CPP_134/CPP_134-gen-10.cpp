#include<stdio.h>
#include<ctype.h>
#include<string.h>
using namespace std;
bool check_if_last_char_is_a_letter(string txt){
    if(txt.length()==0){
        return false;
    }
    char last_char=txt[txt.length()-1];
    if(isalpha(last_char)&&last_char!=' '){
        return true;
    }
    return false;
}
请问代码逻辑有问题吗？


