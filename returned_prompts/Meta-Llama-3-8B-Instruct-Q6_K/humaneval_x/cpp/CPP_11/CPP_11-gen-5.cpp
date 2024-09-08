    string res;
    if(a.length()!=b.length())
        return "Strings are of different length";
    for(int i=0;i<a.length();i++){
        if(a[i]==b[i])
            res+="0";
        else
            res+="1";
    }
    return res;
}

