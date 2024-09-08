    vector<int> result;
    int beats = 0;
    for (char c : music_string) {
        if (c == 'o') {
            beats += 4;
        } else if (c == '|') {
            beats = 0;
        } else if (c == '.') {
            beats = 1;
        }
        result.push_back(beats);
    }
    return result;
}

B:
    vector<int> parse_music(string music_string) {
        vector<int> result;
        for (int i = 0; i < music_string.size(); i++) {
            if (music_string[i] == 'o') {
                result.push_back(4);
            } else if (music_string[i] == '|') {
                if (result.size() > 0) {
                    result.pop_back();
                }
            } else if (music_string[i] == '.') {
                if (result.size() > 0) {
                    result.back() = 1;
                }
            }
        }
        return result;
    }
}
C:
    vector<int> parse_music(string music_string) {
        vector<int> result;
        for (char c : music_string) {
            if (c == 'o') {
                result.push_back(4);
            } else if (c == '|') {
                if (result.size() > 0) {
                    result.back() = 2;
                }
            } else if (c == '.') {
                if (result.size() > 0) {
                    result.back() = 1;
                }
            }
        }
        return result;
    }
D:
    vector<int> parse_music(string music_string) {
        vector<int> result;
        for (char c : music_string) {
            if (c == 'o') {
                result.push_back(4);
            } else if (c == '|') {
                if (result.size() > 0) {
                    result.back() = 2;
                }
            } else if (c == '.') {
                if (result.size() > 0) {
                    result.back() = 1;
                }
            }
        }
        return result;
    }
E:
    vector<int> parse_music(string music_string) {
        vector<int> result;
        for (char c : music_string) {
            if (c == 'o') {
                result.push_back(4);
            } else if (c == '|') {
                if (result.size() > 0