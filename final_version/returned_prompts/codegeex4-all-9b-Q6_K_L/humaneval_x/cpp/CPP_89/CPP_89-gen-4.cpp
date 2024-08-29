#include <iostream>
using namespace std;

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);

    // Encrypt the string
    for (int i = 0; i < input.length(); i++) {
        // Convert char to ASCII value
        int asciiValue = int(input[i]);

        // Check if the character is a lowercase letter
        if (asciiValue >= 97 && asciiValue <= 122) {
            asciiValue += 2 * 2; // Shift the character down by two places

            // If the character goes past 'z', wrap around to 'a'
            if (asciiValue > 122) {
                asciiValue -= 26;
            }

            // Convert ASCII value back to char
            input[i] = char(asciiValue);
        }
        // Check if the character is an uppercase letter
        else if (asciiValue >= 65 && asciiValue <= 90) {
            asciiValue += 2 * 2; // Shift the character down by two places

            // If the character goes past 'Z', wrap around to 'A'
            if (asciiValue > 90) {
                asciiValue -= 26;
            }

            // Convert ASCII value back to char
            input[i] = char(asciiValue);
        }
    }

    cout << "Encrypted string: " << input << endl;

    return 0;
}

C:
#include <iostream>
#include <string>
using namespace std;

string encrypt(string s) {
    string encrypted = "";
    for (int i = 0; i < s.length(); i++) {
        char c = s[i];
        if (isalpha(c)) {
            int shift = 2 * 2;
            c = (islower(c)) ? 'a' : 'A';
            c = (c + (c - 'a' + shift) % 26);
        }
        encrypted += c;
    }
    return encrypted;
}

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);

    string encrypted = encrypt(input);
    cout << "Encrypted string: " << encrypted << endl;

    return 0;
}