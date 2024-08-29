/*
Write a function that takes a string as a parameter and returns a new string
with all the vowels removed.
Example:
remove_vowels("hello") == "hll"
remove_vowels("world") == "wrld"
*/
#include<stdio.h>
#include<math.h>
#include<string.h>
using namespace std;
char* remove_vowels(char* s){
char* res = new char[strlen(s)];
int j = 0;
for(int i = 0;i<strlen(s);i++){
if(s[i] != 'a' && s[i] != 'e' && s[i] != 'i' && s[i] != 'o' && s[i] != 'u' && s[i] != 'A' && s[i] != 'E' && s[i] != 'I' && s[i] != 'O' && s[i] != 'U'){
res[j] = s[i];
j++;
}
}
res[j] = '\0';
return res;
}
