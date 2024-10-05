    vector<bool> appeared(256,false);
    int count=0;
    for(int i=0;i<str.size();i++){
        if(!appeared[tolower(str[i])]){
            appeared[tolower(str[i])]=true;
            count++;
        }
    }
    return count;
}

