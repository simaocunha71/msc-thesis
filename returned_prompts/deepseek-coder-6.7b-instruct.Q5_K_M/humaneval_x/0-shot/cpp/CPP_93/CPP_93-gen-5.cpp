    for(int i = 0; i < message.size(); i++){
        if(islower(message[i])){
            message[i] = toupper(message[i]);
        }else{
            message[i] = tolower(message[i]);
        }
        if(message[i] == 'a'){
            message[i] = 'C';
        }else if(message[i] == 'e'){
            message[i] = 'G';
        }else if(message[i] == 'i'){
            message[i] = 'K';
        }else if(message[i] == 'o'){
            message[i] = 'Q';
        }else if(message[i] == 'u'){
            message[i] = 'W';
        }else if(message[i] == 'A'){
            message[i] = 'C';
        }else if(message[i] == 'E'){
            message[i] = 'G';
        }else if(message[i] == 'I'){
            message[i] = 'K';
        }else if(message[i] == 'O'){
            message[i] = 'Q';
        }else if(message[i] == 'U'){
            message[i] = 'W';
        }
    }
    return message;
}

int main(){
    string message;
    cout<<"Enter message: ";
    getline(cin,message);
    cout<<"Encoded message: "<<encode(message);
    return 0;
}
*/

#include <iostream>
#include <string>

using namespace std;

string encode(string message) {
    string vowels = "aeiouAEIOU";
    string alphabet = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";

    for (int i = 0; i < message.size(); i++) {
        if (vowels.find(message[i]) != string::npos) {
            message[i] = alphabet