#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string encrypt(string s) {
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    string encrypted = s;

    for (int i = 0; i < s.length(); i++) {
        char c = s[i];

        if (isalpha(c)) {
            int index = alphabet.find(tolower(c));
            if (index == -1) {
                encrypted[i] = c;
            } else {
                char newChar = alphabet[(index + 4) % 26];
                if (islower(c)) {
                    encrypted[i] = newChar;
                } else {
                    encrypted[i] = toupper(newChar);
                }
            }
        } else {
            encrypted[i] = c;
        }
    }

    return encrypted;
}

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);
    string encryptedString = encrypt(input);
    cout << "Encrypted string: " << encryptedString << endl;
    return 0;
}
B:
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string encrypt(string s) {
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    string encrypted = s;

    for (int i = 0; i < s.length(); i++) {
        char c = s[i];

        if (isalpha(c)) {
            int index = alphabet.find(tolower(c));
            if (index == -1) {
                encrypted[i] = c;
            } else {
                char newChar = alphabet[(index + 4) % 26];
                if (islower(c)) {
                    encrypted[i] = newChar;
                } else {
                    encrypted[i] = toupper(newChar);
                }
            }
        } else {
            encrypted[i] = c;
        }
    }

    return encrypted;
}

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);
    string encryptedString = encrypt(input);
    cout << "Encrypted string: " << encryptedString << endl;
    return 0;
}
C:
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string encrypt(string s) {
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    string encrypted = s;

    for (int i = 0; i < s.length(); i++) {
        char c = s[i];

        if (isalpha(c)) {
            int index