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
#include<ctype.h>
#include<string>
#include<algorithm>
using namespace std;
string encode(string message){

    string encoded = "";
    for (int i = 0; i < message.length(); i++){
        char c = message[i];
        if (isalpha(c)){
            if (islower(c)){
                c = toupper(c);
            }
            else {
                c = tolower(c);
            }
        }

        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
            c = c + 2;
        }
        encoded += c;
    }

    return encoded;

}

B:
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
#include<ctype.h>
#include<string>
#include<algorithm>
using namespace std;
string encode(string message){

    string encoded = "";
    for (int i = 0; i < message.length(); i++){
        char c = message[i];
        if (isalpha(c)){
            if (islower(c)){
                c = toupper(c);
            }
            else {
                c = tolower(c);
            }
        }

        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
            c = c + 2;
        }
        encoded += c;
    }

    return encoded;

}

C:
/*
Write a function that takes a message, and encodes in such a 
way that it swaps case of all letters, replaces all vowels in 
the message with the letter that appears 2 places ahead of that 
vowel in the