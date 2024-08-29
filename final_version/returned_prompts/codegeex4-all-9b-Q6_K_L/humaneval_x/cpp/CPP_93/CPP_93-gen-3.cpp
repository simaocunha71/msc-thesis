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
        if(message[i]>='a'&&message[i]<='z'){
            message[i]-=32;
        }
        else if(message[i]>='A'&&message[i]<='Z'){
            message[i]+=32;
        }
        if(message[i]=='a'||message[i]=='e'||message[i]=='i'||message[i]=='o'||message[i]=='u'){
            if(message[i]=='a'){
                message[i]='c';
            }
            else if(message[i]=='e'){
                message[i]='g';
            }
            else if(message[i]=='i'){
                message[i]='k';
            }
            else if(message[i]=='o'){
                message[i]='q';
            }
            else if(message[i]=='u'){
                message[i]='w';
            }
        }
    }
    return message;
}

int main(){
    string message="This is a message";
    string encoded_message=encode(message);
    cout<<encoded_message<<endl;
    return 0;
}