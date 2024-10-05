    for(int i = 0; i < message.length(); i++) {
        if(message[i] >= 'a' && message[i] <= 'z') {
            message[i] = message[i] - 'a' + 'A';
        }
        else if(message[i] >= 'A' && message[i] <= 'Z') {
            message[i] = message[i] - 'A' + 'a';
        }
        else if(message[i] == 'a') {
            message[i] = 'c';
        }
        else if(message[i] == 'e') {
            message[i] = 'g';
        }
        else if(message[i] == 'i') {
            message[i] = 'k';
        }
        else if(message[i] == 'o') {
            message[i] = 'u';
        }
        else if(message[i] == 'u') {
            message[i] = 'i';
        }
        else if(message[i] == 't') {
            message[i] = 'w';
        }
    }
    return message;
}

int main() {
    printf("%s",encode("test"));
    return 0;
}
















































































































































































































