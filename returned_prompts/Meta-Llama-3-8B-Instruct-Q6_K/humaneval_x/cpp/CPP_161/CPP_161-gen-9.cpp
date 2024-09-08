    for(int i = 0; i < s.length(); i++){
        if(isalpha(s[i])){
            if(islower(s[i])) s[i] = toupper(s[i]);
            else s[i] = tolower(s[i]);
        }
    }
    if(s.length() == 0) reverse(s.begin(), s.end());
    return s;
}

