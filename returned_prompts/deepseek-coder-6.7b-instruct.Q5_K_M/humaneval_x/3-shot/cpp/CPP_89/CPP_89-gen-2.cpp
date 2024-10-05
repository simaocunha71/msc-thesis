    string encrypted="";
    for(int i=0;i<s.length();i++){
        if(isupper(s[i])) encrypted+=char(((s[i]-'A'+2*2)%26)+'A');
        else if(islower(s[i])) encrypted+=char(((s[i]-'a'+2*2)%26)+'a');
    }
    return encrypted;
}


