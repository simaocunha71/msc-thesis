    vector<int> beats;
    int i;
    for (i=0;i<music_string.size();i++){
        switch(music_string[i]){
            case 'o': beats.push_back(4); break;
            case '|': beats.push_back(2); break;
            case '.': beats.push_back(1); break;
        }
    }
    return beats;
}


