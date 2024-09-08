vector<int> res;
for (int i = 0; i < music_string.size(); i++) {
    if (music_string[i] == 'o') {
        res.push_back(4);
    } else if (music_string[i] == '|') {
        if (music_string[i-1] == '.') {
            res.push_back(1);
        } else {
            res.push_back(2);
        }
    }
}
return res;
}

C:
#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> result;
    map<char, int> note_map = {{'o', 4}, {'o|', 2}, {'.|', 1}};
    
    for (int i = 0; i < music_string.size(); i++) {
        string note;
        while (i < music_string.size() && music_string[i] != '|') {
            note += music_string[i];
            i++;
        }
        result.push_back(note_map[note]);
    }
    return result;
}

E:
#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> result;
    map<string, int> note_map = {{"o", 4}, {"o|", 2}, {".|", 1}};
    string note;
    
    for (char c : music_string) {
        note += c;
        if (note_map.find(note) != note_map.end()) {
            result.push_back(note_map[note]);
            note.clear();
        }
    }
    return result;
}

P:
#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> result;
    map<string, int> note_map = {{"o", 4}, {"o|", 2}, {".|", 1}};
    string note;
    for (char c : music_string) {
        note += c;
        if (note_map.count(note) > 0) {
            result.push_back(note_map[note]);
            note.clear();
        }
    }
    return result;
}

R:
#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> result;
   