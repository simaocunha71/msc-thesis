#include <vector>
#include <string>
#include <sstream>
#include <iterator>
using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> notes;
    stringstream ss(music_string);
    string note;
    while (getline(ss, note, ' ')) {
        if (note == "o") {
            notes.push_back(4);
        } else if (note == "o|") {
            notes.push_back(2);
        } else if (note == ".|") {
            notes.push_back(1);
        }
    }
    return notes;
}

int main() {
    vector<int> beats = parse_music("o o| .| o| o| .| .| .| .| o o");
    for (int beat : beats) {
        printf("%d ", beat);
    }
    return 0;
}
