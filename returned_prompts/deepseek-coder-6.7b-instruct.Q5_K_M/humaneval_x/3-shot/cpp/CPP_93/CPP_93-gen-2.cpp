    string vowels = "aeiouAEIOU";
    string encoded_message = "";
    for(auto chr : message){
        if(isalpha(chr)){
            chr = islower(chr)? toupper(chr) : tolower(chr);
            if(vowels.find(chr)!=string::npos){
                chr = chr+2;
                if(chr>'Z') chr = chr-26;
            }
        }
        encoded_message+=chr;
    }
    return encoded_message;
}

