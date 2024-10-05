    string encrypted = "";
    int i;
    for(i = 0; i < s.length(); i++){
        if(isupper(s[i]))
            encrypted += char(int(s[i] + 2 - 65) % 26 + 65);
        else
            encrypted += char(int(s[i] + 2 - 97) % 26 + 97);
    }
    return encrypted;
}



