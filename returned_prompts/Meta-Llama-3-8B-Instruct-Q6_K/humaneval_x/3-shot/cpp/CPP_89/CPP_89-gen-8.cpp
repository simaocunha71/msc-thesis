    string result;
    for (int i=0;i<s.length();i++){
        char c=s[i];
        if (c>='a' && c<='z'){
            c=(c-'a'+2)%26+'a';
        }
        else if (c>='A' && c<='Z'){
            c=(c-'A'+2)%26+'A';
        }
        result+=c;
    }
    return result;
}  // Corrected this function
}  // Corrected this code block

