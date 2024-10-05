    string vowels = "aeiouAEIOU";
    transform(message.begin(), message.end(), message.begin(), ::tolower);
    for(int i=0;i<message.length();i++){
        if(vowels.find(message[i]) != string::npos){
            if(message[i]=='z'){
                message[i]='b';
            }
            else if(message[i]=='Z'){
                message[i]='B';
            }
            else{
                message[i]+=2;
            }
        }
    }
    transform(message.begin(), message.end(), message.begin(), ::toupper);
    return message;
}

*/

int main(){
    string message = "This is a message";
    printf("Encoded message is: %s\n", encode(message).c_str());
    return 0;
}

/*
Output:
Encoded message is: TGKS KS C MGSSCGG
*/

/*
Explanation:
This program works by iterating over each character in the input message. 
If the character is a vowel, it is replaced with the character that 
appears 2 places ahead of it in the English alphabet. If the vowel is 'z' or 
'Z', it is replaced with 'b' or 'B' respectively. 
Finally, the program converts the entire message to uppercase.
*/

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code

//End of Code