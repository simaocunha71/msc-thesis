string message;
    transform(message.begin(), message.end(), message.begin(), ::tolower);
    for(int i=0; i<message.length(); i++){
        if(message[i] == 'a' || message[i] == 'e' || message[i] == 'i' || message[i] == 'o' || message[i] == 'u' || message[i] == 'A' || message[i] == 'E' || message[i] == 'I' || message[i] == 'O' || message[i] == 'U'){
            message[i] = message[i] + 2;
        }
        else if(message[i] == 'z' || message[i] == 'Z'){
            message[i] = 'b';
        }
        else if(message[i] == 'y' || message[i] == 'Y'){
            message[i] = 'a';
        }
        else if(message[i] == 'x' || message[i] == 'X'){
            message[i] = 'w';
        }
        else if(message[i] == 'w' || message[i] == 'W'){
            message[i] = 'x';
        }
    }

    transform(message.begin(), message.end(), message.begin(), ::toupper);

    return message;
}

int main(){
    string message;
    cout<<"Enter a message: ";
    getline(cin, message);

    string encoded_message = encode(message);

    cout<<"Encoded message: "<<encoded_message<<endl;

    return 0;
}

B:
string encode(string message){
    for(int i=0; i<message.length(); i++){
        if(islower(message[i])){
            message[i] = toupper(message[i]);
        }
        else if(isupper(message[i])){
            message[i] = tolower(message[i]);
        }
        if(message[i]=='a' || message[i]=='A'){
            message[i] = 'c';
        }
        if(message[i]=='e' || message[i]=='E'){
            message[i] = 'g';
        }
        if(message[i]=='i' || message[i]=='I'){
            message[i] = 'k';
        }
        if(message[i]=='o' || message[i]=='O'){
            message[i] = 'q';
        }
        if(message[i]=='u' || message[i]=='U'){
            message[i] = 'w';
        }
    }
    return message;
}

int main(){
    string message;
    cout<<"Enter a message: ";
    getline(cin, message);

    string encoded_message =