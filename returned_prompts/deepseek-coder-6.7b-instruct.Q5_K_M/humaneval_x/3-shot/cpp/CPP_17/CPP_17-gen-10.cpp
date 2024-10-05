    vector<int> beats;
    int i, beat=0;
    for(i=0; i<music_string.length(); i++){
        if(music_string[i] == 'o'){
            if(i+1<music_string.length() && music_string[i+1] == '|'){
                beat = 2;
                i++;
            }
            else beat = 4;
        }
        else if(music_string[i] == '.'){
            if(i+1<music_string.length() && music_string[i+1] == '|'){
                beat = 1;
                i++;
            }
        }
        beats.push_back(beat);
    }
    return beats;
}

