    string vowels="aeiouAEIOU";
    string encoded_message="";
    for(int i=0; i<message.size(); i++){
        if(isalpha(message[i])){
            if(vowels.find(message[i]) != string::npos){
                if(islower(message[i])){
                    encoded_message += char(int('a') + (message[i] - 'a' + 2)%26);
                }
                else{
                    encoded_message += char(int('A') + (message[i] - 'A' + 2)%26);
                }
            }
            else{
                encoded_message += islower(message[i]) ? toupper(message[i]) : tolower(message[i]);
            }
        }
        else{
            encoded_message += message[i];
        }
    }
    return encoded_message;
}


