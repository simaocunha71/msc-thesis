    string result="";
    for(int i=0;i<s.length();i++){
        char c=s[i];
        if(islower(c))
            result+=char(((c-'a'+2*2)%26)+'a');
        else if(isupper(c))
            result+=char(((c-'A'+2*2)%26)+'A');
    }
    return result;
}



