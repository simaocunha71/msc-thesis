    int i = 0;
    int j = text.length() - 1;
    while (i < j) {
        if (text[i] != text[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}
*/

#include <iostream>
#include <string>

bool is_palindrome(std::string text) {
    int i = 0;
    int j = text.length() - 1;
    while (i < j) {
        if (text[i] != text[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

int main() {
    std::string text;
    std::cout << "Enter a string: ";
    std::cin >> text;
    if (is_palindrome(text)) {
        std::cout << "The string is a palindrome.\n";
    } else {
        std::cout << "The string is not a palindrome.\n";
    }
    return 0;
}

/*
