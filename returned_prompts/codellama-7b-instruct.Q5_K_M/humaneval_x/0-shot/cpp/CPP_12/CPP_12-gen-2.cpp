    if(strings.size()==0)
        return "None";
    int maxlen=0;
    int maxpos=0;
    for(int i=0;i<strings.size();i++){
        if(strings[i].size()>maxlen){
            maxlen=strings[i].size();
            maxpos=i;
        }
    }
    return strings[maxpos];
}

