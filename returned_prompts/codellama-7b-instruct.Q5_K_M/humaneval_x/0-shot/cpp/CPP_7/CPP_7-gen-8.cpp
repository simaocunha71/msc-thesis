    for(int i = 0; i < strings.size(); i++){
        if(strings[i].find(substring) != string::npos){
            strings.erase(strings.begin() + i);
        }
    }

    return strings;
}

