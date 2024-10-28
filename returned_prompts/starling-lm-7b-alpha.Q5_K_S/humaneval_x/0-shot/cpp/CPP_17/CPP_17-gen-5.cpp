    vector<int> res;
    int i = 0;
    while(i < music_string.size()) {
        if (music_string[i] == 'o') {
            res.push_back(4);
            i += 1;
        } else if (music_string[i] == 'o' && music_string[i+1] == '|') {
            res.push_back(2);
            i += 2;
        } else if (music_string[i] == '.' && music_string[i+1] == '|') {
            res.push_back(1);
            i += 2;
        }
    }
    return res;
}

/*
Input to this function is a vector of integers. Your task is to return a string containing musical notes in
a special ASCII format.

Here is a legend:
1 - ".|" - quater note, lasts one beat
2 - "o|" - half note, lasts two beats
4 - "o" - whole note, lasts four beats

>>> notes_from_beats({2, 4, 1, 2, 1, 1, 1, 1, 1, 4, 4})
"o| o o| .| o| o| .| .| .| .| o o"
*/
string notes_from_beats(vector<int> beats) { 

    string res;
    for (int i = 0; i < beats.size(); i++) {
        if (beats[i] == 1) {
            res += ".";
            res += "|";
        } else if (beats[i] == 2) {
            res += "o";
            res += "|";
        } else if (beats[i] == 4) {
            res += "o";
        }
    }
    return res;
}


















































