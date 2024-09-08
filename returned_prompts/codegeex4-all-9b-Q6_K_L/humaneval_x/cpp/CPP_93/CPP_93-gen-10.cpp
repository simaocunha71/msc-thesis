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

    string result = "";
    for(int i = 0; i < message.length(); i++){
        char c = message[i];
        if(isupper(c)){
            c = tolower(c);
            if(c == 'a'){
                c = 'c';
            }else if(c == 'e'){
                c = 'g';
            }else if(c == 'i'){
                c = 'k';
            }else if(c == 'o'){
                c = 'q';
            }else if(c == 'u'){
                c = 'w';
            }else{
                result += c;
            }
        }else{
            c = toupper(c);
            if(c == 'A'){
                c = 'C';
            }else if(c == 'E'){
                c = 'G';
            }else if(c == 'I'){
                c = 'K';
            }else if(c == 'O'){
                c = 'Q';
            }else if(c == 'U'){
                c = 'W';
            }else{
                result += c;
            }
        }
    }
    return result;
}

int main(){
    string message = "This is a message";
    string encoded_message = encode(message);
    cout << encoded_message << endl;
    return 0;
}