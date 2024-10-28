    vector<string> vec;
    int i = 0;
    while(i<txt.length()){
        if(txt[i]==' '){
            vec.push_back(txt.substr(0,i));
            txt.erase(0,i+1);
            i = 0;
        }
        i++;
    }
    vec.push_back(txt);
    return vec;
}
