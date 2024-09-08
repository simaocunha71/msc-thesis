    for(int i=0; i<message.length(); i++){
        char c = message[i];
        if(c >= 'a' && c <= 'z'){
            c = (c - 'a' + 2)%26 + 'a';
        }
        else if(c >= 'A' && c <= 'Z'){
            c = (c - 'A' + 2)%26 + 'A';
        }
        message[i] = c;
    }
    for(int i=0; i<message.length(); i++){
        if(message[i] == 'a' || message[i] == 'A'){
            message[i] = 'b';
        }
        else if(message[i] == 'e' || message[i] == 'E'){
            message[i] = 'g';
        }
        else if(message[i] == 'i' || message[i] == 'I'){
            message[i] = 'k';
        }
        else if(message[i] == 'o' || message[i] == 'O'){
            message[i] = 'q';
        }
        else if(message[i] == 'u' || message[i] == 'U'){
            message[i] = 'w';
        }
    }
    transform(message.begin(), message.end(), message.begin(), ::tolower);
    return message;

} 
B:
    for(int i=0; i<message.length(); i++){
        char c = message[i];
        if(c >= 'a' && c <= 'z'){
            c = (c - 'a' + 2)%26 + 'a';
        }
        else if(c >= 'A' && c <= 'Z'){
            c = (c - 'A' + 2)%26 + 'A';
        }
        message[i] = c;
    }
    for(int i=0; i<message.length(); i++){
        char c = message[i];
        if(c == 'a' || c == 'A'){
            message[i] = 'b';
        }
        else if(c == 'e' || c == 'E'){
            message[i] = 'g';
        }
        else if(c == 'i' || c == 'I'){
            message[i] = 'k';
        }
        else if(c == 'o' || c == 'O'){
            message[i] = 'q';
        }
        else if(c == 'u' || c == 'U'){
            message[i] = 'w';
        }
    }
    return message