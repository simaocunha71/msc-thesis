    string vowels="aeiouAEIOU";
    string new_message;
    for(char& c : message){
        if(isalpha(c)){
            c=tolower(c);
            if(vowels.find(c)!=string::npos){
                c=c+2;
            }
            c=toupper(c);
        }
        new_message+=c;
    }
    return new_message;
}


