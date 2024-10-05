    vector<int> characters(128,0);
    int i;
    for  (i=0; i<str.size(); i++){
        characters[tolower(str[i])]=1;
    }
    return count(characters.begin(),characters.end(),1);
}


