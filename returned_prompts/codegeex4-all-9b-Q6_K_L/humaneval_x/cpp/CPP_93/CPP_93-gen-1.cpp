def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for char in message:
        if char in vowels:
            encoded_message += chr(ord(char) + 2)
        else:
            if char.isupper():
                encoded_message += char.lower()
            else:
                encoded_message += char.upper()
    return encoded_message

B:
#include <string>
#include <cctype>

std::string encode(std::string message) {
    std::string encoded_message;
    for (char c : message) {
        if (isalpha(c)) {
            if (islower(c)) {
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    encoded_message += 'c';
                } else if (c == 'y') {
                    encoded_message += 'a';
                } else {
                    encoded_message += c;
                }
            } else {
                if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                    encoded_message += 'C';
                } else if (c == 'Y') {
                    encoded_message += 'A';
                } else {
                    encoded_message += c;
                }
            }
        } else {
            encoded_message += c;
        }
    }
    return encoded_message;
}

C:
def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for char in message:
        if char.lower() in vowels:
            encoded_message += chr(ord(char) + 2)
        elif char.isupper():
            encoded_message += char.lower()
        else:
            encoded_message += char.upper()
    return encoded_message

D:
def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for char in message:
        if char.lower() in vowels:
            encoded_message += chr(ord(char) + 2)
        elif char.isupper():
            encoded_message += char.lower()
        else:
            encoded_message += char.upper()
    return encoded_message

E:
def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for char in message:
        if char.lower() in vowels:
            encoded