#include <string>
#include <sstream>
#include <vector>
using namespace std;

vector<int> parse_music(string music_string) {
    stringstream ss(music_string);
    string token;
    vector<int> result;

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

int main() {
    vector<int> beats = parse_music("o o| .| o| o| .| .| .| .| o o");
    for (int beat : beats) {
        printf("%d ", beat);
    }
    printf("\n");
    return 0;
}
