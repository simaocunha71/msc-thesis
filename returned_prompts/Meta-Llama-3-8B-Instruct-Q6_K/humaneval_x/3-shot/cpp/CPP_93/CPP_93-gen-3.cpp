    string result;
    for (int i=0;i<message.length();i++){
        char c = message[i];
        if (isalpha(c)){
            if (islower(c)){
                c = 'a' + (c - 'a' + 2) % 26;
            }else{
                c = 'A' + (c - 'A' + 2) % 26;
            }
            if (c == 'a' || c == 'A') c = 'a';
            if (c == 'e' || c == 'E') c = 'g';
            if (c == 'i' || c == 'I') c = 'k';
            if (c == 'o' || c == 'O') c = 'q';
            if (c == 'u' || c == 'U') c = 'w';
        }
        if (isupper(c)) result += tolower(c);
        else result += toupper(c);
    }
    return result;
}