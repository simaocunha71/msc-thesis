#include<stdio.h>
#include<string>
#include<ctype.h>
using namespace std;
bool check_if_last_char_is_a_letter(string txt){
    int i=txt.length();
    char ch=txt[i-1];
    if(isalpha(ch) && txt[i]==' ')
        return true;
    return false;
}
