#include <unordered_set>
#include <algorithm>
#include <cctype>
#include <iostream>
using namespace std;

int count_distinct_characters(string str) {
    unordered_set<char> distinct_chars;
    for (char c : str) {
        distinct_chars.insert(tolower(c));
    }
    return distinct_chars.size();
}

int main() {
    cout << count_distinct_characters("xyzXYZ") << endl;  // Outputs 3
    cout << count_distinct_characters("Jerry") << endl;   // Outputs 4
    return 0;
}

The above code uses an unordered_set to store unique characters, tolower() is used to convert characters to lowercase to ensure case insensitivity. The size() function of unordered_set returns the number of distinct characters in the string.