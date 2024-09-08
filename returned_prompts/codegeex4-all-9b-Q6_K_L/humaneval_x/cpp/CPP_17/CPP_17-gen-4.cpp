#include <vector>
#include <string>

using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> notes;
    for (int i = 0; i < music_string.size(); ++i) {
        if (music_string[i] == 'o') {
            notes.push_back(4);
            ++i;
            if (music_string[i] == '|') ++i;
        } else if (music_string[i] == '.') {
            notes.push_back(1);
            ++i;
            if (music_string[i] == '|') ++i;
        }
    }
    return notes;
}
