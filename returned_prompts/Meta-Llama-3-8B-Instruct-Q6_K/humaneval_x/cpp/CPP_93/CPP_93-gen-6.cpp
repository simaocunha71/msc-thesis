    for(int i = 0; i<message.length(); i++){
        if(isalpha(message[i])){
            if(isupper(message[i])){
                message[i] = 'a' + (message[i] - 'A');
            }
            else{
                message[i] = 'A' + (message[i] - 'a');
            }
        }
        else{
            continue;
        }
        if(message[i] == 'a' || message[i] == 'e' || message[i] == 'i' || message[i] == 'o' || message[i] == 'u'){
            if(message[i] == 'a'){
                message[i] = 'c';
            }
            else if(message[i] == 'e'){
                message[i] = 'g';
            }
            else if(message[i] == 'i'){
                message[i] = 'k';
            }
            else if(message[i] == 'o'){
                message[i] = 'q';
            }
            else if(message[i] == 'u'){
                message[i] = 'w';
            }
        }
    }
    return message;
}

int main(){
    string message = "This is a message";
    string result = encode(message);
    printf("%s\n",result.c_str());
    return 0;
}
```

Explanation:
This function takes a string message as input and returns the encoded string. 

It iterates over each character in the message. If the character is a letter, it swaps its case by subtracting the ASCII value of 'A' or 'a' from the character and adding the result to 'a' or 'A'. If the character is a vowel, it replaces it with the letter that appears 2 places ahead in the alphabet. 

The function continues until it has processed all characters in the message. The encoded message is then returned. 

In the main function, we test the encode function with the message "This is a message" and print the result. 

Note: This code assumes that the input is a valid string and only contains letters. If the input may contain other characters, you should add error checking code to handle this. 

Also, this code does not handle uppercase vowels correctly. It should be modified to handle them correctly. 

Here is the corrected code:
```c++
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string encode(string message){

    for(int i = 0; i<message.length(); i++){
        if(isalpha(message[i])){
            if(is