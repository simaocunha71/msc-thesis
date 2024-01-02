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
    int size = str.size();
    if (str == "")return false;
    for (int i=1;i<size/2+1;i++) {
        if (str[i] != '[' && str[i-1]!='[') 
            return false;
        else{if(str[i]=='[')
            str = str.replace(i,1,'');
        }
    }
   int size2=size/2+1;
   if (str == "")return true;
   bool is_nested = false;
   for (int i=0;i<size2-1;i++) {
       if(str[i]=='[]') 
           str = str.replace(i,1,'');
        else{if(str[i]!=']' && str[i+1]==']') 
            is_nested = true;
            return is_nested;
    }
return false; 
}
int main(){
   if (is_nested("[]") ==true){
       printf("\n True");
   }else {
       printf("\n False");
   }
   return 0;
}