#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> parse_music(const string& music_string) {
    vector<int> result;
    string note;
    for (int i = 0; i < music_string.length(); ++i) {
        if (music_string[i] == 'o') {
            note += music_string[i];
            if (i + 1 < music_string.length() && music_string[i + 1] == '|') {
                i++;
                note += music_string[i];
            }
            if (note == "o|") {
                result.push_back(2);
            } else if (note == ".|") {
                result.push_back(1);
            } else if (note == "o") {
                result.push_back(4);
            }
            note = "";
        }
    }
    return result;
}

int main() {
    string music_string = "o o| .| o| o| .| .| .| .| o o";
    vector<int> result = parse_music(music_string);
    for (int i = 0; i < result.size(); ++i) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
