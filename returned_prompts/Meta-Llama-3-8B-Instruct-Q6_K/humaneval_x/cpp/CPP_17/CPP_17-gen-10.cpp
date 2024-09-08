    vector<int> beat_vector;

    for(int i = 0; i < music_string.size(); i++) {
        if(music_string[i] == 'o') {
            beat_vector.push_back(4);
        } else if(music_string[i] == '|') {
            if(i > 0 && music_string[i-1] == '.') {
                beat_vector.push_back(1);
            } else {
                beat_vector.push_back(2);
            }
        } else if(music_string[i] == '.') {
            beat_vector.push_back(1);
        }
    }

    return beat_vector;
}
