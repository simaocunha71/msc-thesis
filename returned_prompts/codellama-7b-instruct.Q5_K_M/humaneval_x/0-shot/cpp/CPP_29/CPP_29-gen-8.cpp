    for(int i = 0; i < strings.size(); i++){
        if(strings[i].find(prefix) == 0){
            strings.erase(strings.begin() + i);
            i--;
        }
    }
    return strings;
}
