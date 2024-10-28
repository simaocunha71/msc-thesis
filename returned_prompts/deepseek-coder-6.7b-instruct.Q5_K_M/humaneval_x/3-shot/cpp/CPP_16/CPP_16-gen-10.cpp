    vector<int> chars(128,0);
    int i;
    for  (i=0;i<str.length();i++)
    chars[tolower(str[i])]=1;

    return count(chars.begin(),chars.end(),1);
}


