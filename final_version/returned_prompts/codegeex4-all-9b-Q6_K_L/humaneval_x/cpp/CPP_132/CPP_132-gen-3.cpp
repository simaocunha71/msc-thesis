/*
Create a function that takes a string as input which contains only square brackets.
The function should return true if and only if there is a valid subsequence of brackets
where at least one bracket in the subsequence is nested.

is_nested("[[]]") ➞ true
is_nested("[]]]]]]][[[[[]") ➞ false
is_nested("[][]") ➞ false
is_nested("[]") ➞ false
is_nested("[[][]]") ➞ true
is_nested("[[]][[") ➞ true
*/
#include<stdio.h>
#include<string>
using namespace std;
bool is_nested(string str){

    int n = str.length();
    int open = 0, close = 0;
    for(int i=0; i<n; i++){
        if(str[i] == '[') open++;
        else if(str[i] == ']') close++;
    }
    if(open != close) return false;

    int i=0, j=n-1;
    while(i<j){
        if(str[i] == '[' && str[j] == ']'){
            i++;
            j--;
        }
        else if(str[i] == '['){
            i++;
        }
        else if(str[j] == ']'){
            j--;
        }
        else{
            return true;
        }
    }
    return false;
}
int main(){
    string str;
    cin>>str;
    bool res = is_nested(str);
    if(res) cout<<"true";
    else cout<<"false";
    return 0;
}
