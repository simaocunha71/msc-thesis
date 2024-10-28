    string vowels = "aeiouAEIOU";
    string encoded_message = "";
    for (char c : message){
        if (isalpha(c)){
            c = islower(c) ? toupper(c) : tolower(c);
            if (vowels.find(c) != string::npos){
                c += 2;
                if (c > 'Z'){
                    c -= 26;
                }
            }
        }
        encoded_message += c;
    }
    return encoded_message;
}


