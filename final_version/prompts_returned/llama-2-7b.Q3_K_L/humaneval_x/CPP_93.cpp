/*
Write a function that takes a message, and encodes in such a 
way that it swaps case of all letters, replaces all vowels in 
the message with the letter that appears 2 places ahead of that 
vowel in the english alphabet. 
Assume only letters. 

Examples:
>>> encode('test")
"TGST"
>>> encode("This is a message")
'tHKS KS C MGSSCGG"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string encode(string message){
	int pos = 0, cnt = 1 ;
    string s = "abcdefghijklmnopqrstuvwxyz";   //string to be encodede
    for(int i=0;i<message.length();++i) {
        if (message[i]=='a'|| message[i]=='e' || 
            message[i]=='I'|| message[i]=='o'|| 
            message[i]=='u')
            
           cnt++;
        pos = s.find(message[i]) + (cnt-1);   //pos of 'a' after 'e', etc, etc..
        
        if(pos!=s.length())//if pos is not at the end of string
            message[i] = s[pos];  //assign the encodede letter to message[i]
    }
    return message;
}
int main() {
    int i=1,j;
    char b[50],a[50];
   scanf("%c",&b);
    scanf("%s",&a);
     for(; j<i+46;++j)
       a[j]=b[j-47]%26+'a';
    printf("%d\n",j-50);

}