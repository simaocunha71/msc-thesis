    if(strings.empty()) return NULL;
    string longest=strings[0];
    for(int i=1;i<strings.size();i++){
        if(strings[i].length()>longest.length())
            longest=strings[i];
    }
    return longest;
}



