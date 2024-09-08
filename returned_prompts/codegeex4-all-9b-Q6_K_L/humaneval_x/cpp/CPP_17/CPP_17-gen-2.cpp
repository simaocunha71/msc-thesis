#include <vector>
#include <string>
#include <sstream>
using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> result;
    stringstream ss(music_string);
    string token;
    while (getline(ss, token, ' ')) {
        if (token == "o") {
            result.push_back(4);
        } else if (token == "o|") {
            result.push_back(2);
        } else if (token == ".|") {
            result.push_back(1);
        }
    }
    return result;
}