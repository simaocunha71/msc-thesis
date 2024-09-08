#include<stdio.h>
#include<string.h>
bool check_if_last_char_is_a_letter(char* txt){
    int n=strlen(txt);
    if(n==0){
        return false;
    }
    char ch=txt[n-1];
    if((ch>='a' && ch<='z')||(ch>='A' && ch<='Z')){
        if((n>=2 && txt[n-2]!=' ')||(n==1)){
            return true;
        }
    }
    return false;
}
int main(){
    check_if_last_char_is_a_letter("apple pie");
    check_if_last_char_is_a_letter("apple pi e");
    check_if_last_char_is_a_letter("apple pi e ");
    check_if_last_char_is_a_letter("");
    return 0;
}
B:
#include<stdio.h>
#include<string.h>
bool check_if_last_char_is_a_letter(char* txt){
    int n=strlen(txt);
    if(n==0){
        return false;
    }
    char ch=txt[n-1];
    if((ch>='a' && ch<='z')||(ch>='A' && ch<='Z')){
        if((n>=2 && txt[n-2]!=' ')||(n==1)){
            return true;
        }
    }
    return false;
}
int main(){
    check_if_last_char_is_a_letter("apple pie");
    check_if_last_char_is_a_letter("apple pi e");
    check_if_last_char_is_a_letter("apple pi e ");
    check_if_last_char_is_a_letter("");
    return 0;
}
C:
#include<stdio.h>
#include<string.h>
bool check_if_last_char_is_a_letter(char* txt){
    int n=strlen(txt);
    if(n==0){
        return false;
    }
    char ch=txt[n-1];
    if((ch>='a' && ch<='z')||(ch>='A' && ch<='Z')){
        if((n>=2 && txt[n-2]!=' ')||(n==1)){
            return true;
        }
    }
    return false;
}
int main(){
    check_if_last_char_is_a_letter("apple pie");
    check_if_last_char_is_a_letter("apple pi e");
    check_if_last_char_is_a_letter("apple pi e ");
    check_if_last_char_is_a_letter("");
    return 0;
}
D:
#include<stdio.h>
#include<string.h>
bool check_if_last_char_is_a_letter(char* txt){
    int n