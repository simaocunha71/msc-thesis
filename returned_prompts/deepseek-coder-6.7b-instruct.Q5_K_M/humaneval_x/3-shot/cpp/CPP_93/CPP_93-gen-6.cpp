    string result="";
    for (int i=0; i<message.length(); i++){
        char c = message[i];
        if (isalpha(c)){
            if (islower(c)){
                if (c>='a' && c<='z'){
                    if (c=='a') c='c';
                    else if (c=='e') c='g';
                    else if (c=='i') c='k';
                    else if (c=='o') c='q';
                    else if (c=='u') c='w';
                    else c = toupper(c);
                }
            }
            else if (isupper(c)){
                if (c>='A' && c<='Z'){
                    if (c=='A') c='C';
                    else if (c=='E') c='G';
                    else if (c=='I') c='K';
                    else if (c=='O') c='Q';
                    else if (c=='U') c='W';
                    else c = tolower(c);
                }
            }
        }
        result+=c;
    }
    return result;
}

