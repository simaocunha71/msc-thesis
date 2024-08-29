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
    for(int i=0;i<message.length();i++){
        char c=message[i];
        if(c>='a'&&c<='z')
            c-=32;
        else if(c>='A'&&c<='Z')
            c+=32;
        if(c=='a')
            c='c';
        else if(c=='e')
            c='g';
        else if(c=='i')
            c='k';
        else if(c=='o')
            c='q';
        else if(c=='u')
            c='w';
        message[i]=c;
    }
    return message;
}

