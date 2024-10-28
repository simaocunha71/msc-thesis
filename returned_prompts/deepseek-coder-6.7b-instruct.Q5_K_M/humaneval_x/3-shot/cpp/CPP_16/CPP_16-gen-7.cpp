    vector<int> char_set(128,0);
    int i;
    for  (i=0;i<str.length();i++)
    char_set[tolower(str[i])]=1;

    return count(char_set.begin(),char_set.end(),1);
}


