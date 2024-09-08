    vector<int> result;
    for (int i = 0; i < music_string.size(); i++) {
        if (music_string[i] == 'o') {
            result.push_back(4);
        } else if (music_string[i] == '|') {
            if (i > 0 && music_string[i-1] == '.') {
                result.push_back(1);
            } else {
                result.push_back(2);
            }
        } else if (music_string[i] == '.') {
            result.push_back(1);
        }
    }
    return result;
}
B:
    vector<int> parse_music(string music_string) {
        vector<int> result;
        for (int i = 0; i < music_string.size(); i++) {
            int beats = 4; // default is whole note
            if (music_string[i] == '|') {
                beats = 2; // half note or quater note
                if (i > 0 && music_string[i-1] == '.') {
                    beats = 1; // quater note
                }
            }
            result.push_back(beats);
        }
        return result;
    }
C:
    vector<int> parse_music(string music_string) {
        vector<int> result;
        for (int i = 0; i < music_string.size(); i++) {
            if (music_string[i] == 'o') {
                result.push_back(4);
            } else if (music_string[i] == 'o' && music_string[i+1] == '|') {
                result.push_back(2);
                i++;
            } else if (music_string[i] == '.') {
                result.push_back(1);
            } else if (music_string[i] == '|' && music_string[i-1] == '.') {
                result.push_back(1);
                i--;
            }
        }
        return result;
    }
D:
    vector<int> parse_music(string music_string) {
        vector<int> result;
        for (int i = 0; i < music_string.size(); i++) {
            if (music_string[i] == 'o') {
                result.push_back(4);
            } else if (music_string[i] == 'o' && music_string[i+1] == '|') {
                result.push_back(2);
            } else if (music_string[i] == '.') {
                result.push_back(1);
            }
        }
        return result;
    }D:
   