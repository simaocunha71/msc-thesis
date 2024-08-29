#include <iostream>
#include <string>
using namespace std;

int how_many_times(string str, string substring) {
    int count = 0;
    size_t pos = 0;

    while ((pos = str.find(substring, pos)) != string::npos) {
        count++;
        pos += substring.length();
    }

    return count;
}

int main() {
    string str = "aaaa";
    string substring = "aa";
    cout << how_many_times(str, substring) << endl; // Output: 3
    return 0;
}

B:
#include <iostream>
#include <string>
using namespace std;

int how_many_times(string str, string substring) {
    int count = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == substring[0]) {
            bool match = true;
            for (int j = 0; j < substring.length(); j++) {
                if (str[i+j] != substring[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                count++;
            }
        }
    }
    return count;
}

int main() {
    string str = "aaaa";
    string substring = "aa";
    cout << how_many_times(str, substring) << endl; // Output: 3
    return 0;
}

C:
#include <iostream>
#include <string>
using namespace std;

int how_many_times(string str, string substring) {
    int count = 0;
    for (int i = 0; i <= str.length() - substring.length(); i++) {
        bool match = true;
        for (int j = 0; j < substring.length(); j++) {
            if (str[i+j] != substring[j]) {
                match = false;
                break;
            }
        }
        if (match) {
            count++;
        }
    }
    return count;
}

int main() {
    string str = "aaaa";
    string substring = "aa";
    cout << how_many_times(str, substring) << endl; // Output: 3
    return 0;
}

D:
#include <iostream>
#include <string>
using namespace std;

int how_many_times(string str, string substring) {
    int count = 0;
    for (int i = 0; i <= str.length() - substring.length(); i++) {
        if (str.substr(i, substring.length()) == substring