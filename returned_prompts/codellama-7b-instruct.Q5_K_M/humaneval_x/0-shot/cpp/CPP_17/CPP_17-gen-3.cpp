    vector<int> res;
    for(int i = 0; i < music_string.size(); i++){
        if(music_string[i] == 'o'){
            res.push_back(4);
        }
        else if(music_string[i] == '|'){
            res.push_back(2);
        }
        else if(music_string[i] == '.'){
            res.push_back(1);
        }
        else{
            continue;
        }
    }
    return res;
}