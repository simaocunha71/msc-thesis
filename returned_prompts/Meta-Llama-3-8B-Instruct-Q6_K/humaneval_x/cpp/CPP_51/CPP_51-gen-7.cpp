    string result = text;
    for(int i = 0; i < text.length(); i++){
        if(text[i] == 'a' || text[i] == 'e' || text[i] == 'i' || text[i] == 'o' || text[i] == 'u' ||
           text[i] == 'A' || text[i] == 'E' || text[i] == 'I' || text[i] == 'O' || text[i] == 'U'){
            result.erase(i, 1);
            i--;
        }
    }
    return result;
}
int main()
{
    string text;
    cout << "Enter the text: ";
    cin >> text;
    cout << "Text after removing vowels: " << remove_vowels(text) << endl;
    return 0;
}

B:
#include <iostream>
#include <string>
using namespace std;

string remove_vowels(string str) {
    string result = "";
    for(int i = 0; i < str.length(); i++) {
        char ch = str[i];
        if(ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u' &&
           ch != 'A' && ch != 'E' && ch != 'I' && ch != 'O' && ch != 'U') {
            result += ch;
        }
    }
    return result;
}

int main() {
    string str;
    cout << "Enter a string: ";
    cin >> str;
    cout << "String after removing vowels: " << remove_vowels(str) << endl;
    return 0;
}

C:
#include <iostream>
#include <string>
using namespace std;

string remove_vowels(string str) {
    string result = "";
    for(int i = 0; i < str.length(); i++) {
        char ch = str[i];
        if(ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u' &&
           ch != 'A' && ch != 'E' && ch != 'I' && ch != 'O' && ch != 'U') {
            result += ch;
        }
    }
    return result;
}

int main() {
    string str;
    cout << "Enter a string: ";
    getline(cin, str);
    cout << "String after removing vowels: " << remove_vow