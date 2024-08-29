#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){
    int length = brackets.length();
    int count = 0;
    for(int i = 0; i < length; i++){
        if(brackets[i] == '('){
            count++;
        }
        else if(brackets[i] == ')'){
            count--;
        }
    }
    if(count == 0){
        return true;
    }
    else{
        return false;
    }
}