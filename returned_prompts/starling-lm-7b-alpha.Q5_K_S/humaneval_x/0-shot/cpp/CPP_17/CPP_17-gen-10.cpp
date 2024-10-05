    vector<int> result;
    int length = music_string.length();
    for(int i = 0; i < length; i++) {
        if(music_string[i] == 'o') {
            result.push_back(4);
        } else if(music_string[i] == 'o' && music_string[i+1] == '|') {
            result.push_back(2);
        } else if(music_string[i] == '.' && music_string[i+1] == '|') {
            result.push_back(1);
        }
        i++;
    }
    return result;
}

B:

vector<int> parse_music(string music_string) { 
    vector<int> result;
    int length = music_string.length();
    for(int i = 0; i < length; i++) {
        if(music_string[i] == 'o') {
            result.push_back(4);
        } else if(music_string[i] == 'o' && music_string[i+1] == '|') {
            result.push_back(2);
        } else if(music_string[i] == '.' && music_string[i+1] == '|') {
            result.push_back(1);
        } else if(music_string[i] == '.' && music_string[i+1] == '|') {
            result.push_back(1);
        }
        i++;
    }
    return result;
}

C:

vector<int> parse_music(string music_string) { 
    vector<int> result;
    int length = music_string.length();
    for(int i = 0; i < length; i++) {
        if(music_string[i] == 'o' || music_string[i] == 'o' && music_string[i+1] == '|') {
            result.push_back(4);
        } else if(music_string[i] == '.' && music_string[i+