    vector<int> beat_vector;
    int beats = 0;
    string note;
    for (int i = 0; i < music_string.length(); i++) {
        if (music_string[i] == 'o') {
            beats = 4;
            note = "o";
        } else if (music_string[i] == '|') {
            if (note == "o") {
                beats = 2;
            } else if (note == ".") {
                beats = 1;
            }
            note = "";
        } else if (music_string[i] == '.') {
            beats = 1;
            note = ".";
        }
        if (i == music_string.length() - 1) {
            if (note == "o") {
                beat_vector.push_back(4);
            } else if (note == ".") {
                beat_vector.push_back(1);
            }
        }
        beat_vector.push_back(beats);
        beats = 0;
        note = "";
    }
    return beat_vector;
}
