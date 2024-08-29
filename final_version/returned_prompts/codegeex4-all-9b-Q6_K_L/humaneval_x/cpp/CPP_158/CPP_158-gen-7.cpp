#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <string>

using namespace std;

string find_max(vector<string> words) {
    string max_word = "";
    int max_unique_chars = 0;

    for (const string& word : words) {
        unordered_set<char> unique_chars(word.begin(), word.end());
        if (unique_chars.size() > max_unique_chars) {
            max_unique_chars = unique_chars.size();
            max_word = word;
        } else if (unique_chars.size() == max_unique_chars) {
            max_word = min(max_word, word);
        }
    }

    return max_word;
}

int main() {
    vector<string> words = {"name", "of", "string"};
    cout << find_max(words) << endl; // Output: "string"

    words = {"name", "enam", "game"};
    cout << find_max(words) << endl; // Output: "enam"

    words = {"aaaaaaa", "bb", "cc"};
    cout << find_max(words) << endl; // Output: "aaaaaaa"

    return 0;
}

B:
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <string>

using namespace std;

string find_max(vector<string> words) {
    string max_word = "";
    int max_unique_chars = 0;

    for (const string& word : words) {
        unordered_set<char> unique_chars(word.begin(), word.end());
        if (unique_chars.size() > max_unique_chars) {
            max_unique_chars = unique_chars.size();
            max_word = word;
        } else if (unique_chars.size() == max_unique_chars) {
            max_word = min(max_word, word);
        }
    }

    return max_word;
}

int main() {
    vector<string> words = {"name", "of", "string"};
    cout << find_max(words) << endl; // Output: "string"

    words = {"name", "enam", "game"};
    cout << find_max(words) << endl; // Output: "enam"

    words = {"aaaaaaa", "bb", "cc"};
    cout << find_max(words) << endl; // Output: "aaaaaaa"

    return 0;
}

C:
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <string>

using namespace std;

string find_max(vector<string> words) {
