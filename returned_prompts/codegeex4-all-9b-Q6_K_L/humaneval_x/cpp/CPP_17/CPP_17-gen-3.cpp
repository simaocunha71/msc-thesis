#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> result;
    stringstream ss(music_string);
    string note;
    while (getline(ss, note, ' ')) {
        if (note == "o") {
            result.push_back(4);
        } else if (note == "o|") {
            result.push_back(2);
        } else if (note == ".|") {
            result.push_back(1);
        }
    }
    return result;
}

int main() {
    vector<int> result = parse_music("o o| .| o| o| .| .| .| .| o o");
    for (int i : result) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}