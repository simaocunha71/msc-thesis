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

    string output = "";
    for(int i=0; i<message.length(); i++){
        char c = message[i];
        if(c>='a' && c<='z'){
            c = c-('a' - 'A');
        } else if(c>='A' && c<='Z'){
            c = c+('a' - 'A');
        }
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'){
            c = message[i+2];
        }
        output += c;
    }
    return output;
}
string encode(string message){

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
    #include<string>
    #include<algorithm>
    using namespace std;
    string