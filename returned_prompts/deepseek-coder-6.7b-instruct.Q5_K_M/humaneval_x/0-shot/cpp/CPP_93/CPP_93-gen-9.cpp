    string vowels = "aeiouAEIOU";
    string alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for(int i = 0; i < message.size(); i++){
        if(vowels.find(message[i]) != string::npos){
            message[i] = alphabet[alphabet.find(message[i])+2];
        }
        else if(message[i] >= 'a' && message[i] <= 'z'){
            message[i] = message[i] - 32;
        }
        else if(message[i] >= 'A' && message[i] <= 'Z'){
            message[i] = message[i] + 32;
        }
    }

    return message;
}
*/
