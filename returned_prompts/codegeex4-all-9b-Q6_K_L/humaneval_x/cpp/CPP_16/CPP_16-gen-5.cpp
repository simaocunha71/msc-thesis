#include <map>
#include <set>
#include <string>
#include <cctype>

int count_distinct_characters(const string &str) {
    set<char> chars;
    for (auto &c : str) {
        chars.insert(tolower(c));
    }
    return chars.size();
}

