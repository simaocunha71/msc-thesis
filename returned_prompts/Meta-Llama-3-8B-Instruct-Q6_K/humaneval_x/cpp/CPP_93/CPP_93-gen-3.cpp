    string result = "";
    for(int i = 0; i < message.length(); i++){
        char c = message[i];
        if(isalpha(c)){
            if(isupper(c)){
                c = tolower(c);
            }else{
                c = toupper(c);
            }
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
                c += 2;
                if(c > 'z'){
                    c -= 26;
                }
                c = tolower(c);
            }
            result += c;
        }else{
            result += c;
        }
    }
    return result;
}
int main(){
    string message = "This is a message";
    printf("%s\n", encode(message).c_str());
    return 0;
}

C:
#include <stdio.h>
#include <string.h>

char* encode(char* message) {
    char* result = (char*)malloc(strlen(message) * sizeof(char) + 1);
    for(int i = 0; i < strlen(message); i++) {
        char c = message[i];
        if(isalpha(c)) {
            if(isupper(c)) {
                c = tolower(c);
            } else {
                c = toupper(c);
            }
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                c += 2;
                if(c > 'z') {
                    c -= 26;
                }
                c = tolower(c);
            }
            result[i] = c;
        } else {
            result[i] = c;
        }
    }
    result[strlen(message)] = '\0';
    return result;
}

int main() {
    char* message = "This is a message";
    printf("%s\n", encode(message));
    return 0;
}

B:
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char* encode(char* message) {
    char* result = (char*)malloc(strlen(message) * sizeof(char) + 1);
    int i = 0;
    while (*message != '\0') {
        if (isalpha(*message)) {
            char c = *message;
            if (isupper(c)) {
                c = tolower(c);
            } else {
                c = toupper(c);
            }
            if (c == 'a