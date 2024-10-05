    string vowels = "aeiouAEIOU";
    string coded_vowels = "eiouaEIOUA";
    for(int i=0; i<message.size(); i++){
        if(isalpha(message[i])){
            message[i] = islower(message[i]) ? toupper(message[i]) : tolower(message[i]);
        }
        size_t pos = vowels.find(message[i]);
        if (pos != string::npos){
            message[i] = coded_vowels[pos];
        }
    }
    return message;
}


