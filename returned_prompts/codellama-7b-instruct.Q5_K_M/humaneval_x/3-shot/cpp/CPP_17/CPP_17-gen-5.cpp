    vector<int> beats;
    int note_length;
    int i;
    for (i=0;i<music_string.length();i++){
        switch (music_string[i]){
            case 'o':
                note_length=4;
                break;
            case '.':
                note_length=1;
                break;
            case '|':
                note_length=2;
                break;
        }
        beats.push_back(note_length);
    }
    return beats;
}


