    string vowels = "aeiouAEIOU";
    string encoded_message;
    for(char& c : message){
        if(isalpha(c)){
            c = islower(c) ? toupper(c) : tolower(c);
            if(vowels.find(c) != string::npos){
                c = islower(c) ? 'C' : 'c';
            }
        }
        encoded_message += c;
    }
    return encoded_message;
}


