    int i;
    for (i=0; i<s.length(); i++){
        if (isalpha(s[i])){
            if (islower(s[i])){
                s[i] = toupper(s[i]);
            }
            else{
                s[i] = tolower(s[i]);
            }
        }
    }
    if (s.find_first_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == string::npos){
        reverse(s.begin(), s.end());
    }
    return s;
}


