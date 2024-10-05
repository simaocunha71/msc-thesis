    vector<int> notes;
    int i, length = music_string.length();
    for (i=0; i<length; i++) {
        switch (music_string[i]) {
            case 'o': 
                if (music_string[i+1]=='|') {
                    notes.push_back(2);
                    i++;
                }
                else
                    notes.push_back(4);
                break;
            case '|': 
                notes.push_back(1);
                break;
            default: 
                break;
        }
    }
    return notes;
}

