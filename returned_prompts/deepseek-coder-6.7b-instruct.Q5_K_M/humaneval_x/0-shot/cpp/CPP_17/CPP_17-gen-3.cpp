    vector<int> result;
    int i = 0;
    while(i < music_string.size()){
        if(music_string[i] == 'o' && music_string[i+1] == ' '){
            result.push_back(4);
            i += 2;
        }
        else if(music_string[i