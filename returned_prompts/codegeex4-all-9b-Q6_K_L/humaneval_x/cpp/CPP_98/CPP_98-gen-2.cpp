#include <iostream>
#include <string>
using namespace std;

int count_upper(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (i % 2 == 0 && isupper(s[i]) && (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')) {
            count++;
        }
    }
    return count;
}

int main() {
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    int result = count_upper(s);
    cout << "Number of uppercase vowels in even indices: " << result << endl;
    return 0;
}

