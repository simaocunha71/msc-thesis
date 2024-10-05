    string result="";
    for(int i=0;i<s.length();i++){
        if(islower(s[i]))
            result += toupper(s[i]);
        else if(isupper(s[i]))
            result += tolower(s[i]);
        else
            result += s[i];
    }
    if(result.find_first_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == string::npos)
        reverse(result.begin(),result.end());
    return result;
}

