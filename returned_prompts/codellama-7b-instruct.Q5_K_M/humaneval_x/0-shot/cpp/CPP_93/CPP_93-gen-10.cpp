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

    string encoded;
    for(int i=0;i<message.length();i++){
        if(islower(message[i])){
            encoded.push_back(toupper(message[i]));
        }
        else if(isupper(message[i])){
            encoded.push_back(tolower(message[i]));
        }
        else{
            encoded.push_back(message[i]);
        }
    }
    string vowels = "aeiou";
    for(int i=0;i<encoded.length();i++){
        if(vowels.find(encoded[i]) != string::npos){
            if(i+2<encoded.length() && i+2<vowels.length()){
                encoded[i] = vowels[i+2];
            }
        }
    }
    return encoded;
}

int main(){
    string message = "test";
    string encoded = encode(message);
    cout<<encoded;
    return 0;
}
