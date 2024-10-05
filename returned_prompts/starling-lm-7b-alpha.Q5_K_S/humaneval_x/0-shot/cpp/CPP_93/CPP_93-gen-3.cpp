    for(int i = 0; i < message.length(); i++){
        if(message[i] >= 'a' && message[i] <= 'z'){
            message[i] = message[i] - 32;
        }else if(message[i] >= 'A' && message[i] <= 'Z'){
            message[i] = message[i] + 32;
        }
    }

    for(int i = 0; i < message.length(); i++){
        if(message[i] >= 'a' && message[i] <= 'z'){
            message[i] = message[i] + 1;
            if(message[i] > 'z'){
                message[i] = message[i] - 26;
            }
        }else if(message[i] >= 'A' && message[i] <= 'Z'){
            message[i] = message[i] - 1;
            if(message[i] < 'A'){
                message[i] = message[i] + 26;
            }
        }
    }
    return message;
}

int main(){
    string message = "This is a message";
    printf("%s\n", encode(message).c_str());
    return 0;
}




































































































































































































