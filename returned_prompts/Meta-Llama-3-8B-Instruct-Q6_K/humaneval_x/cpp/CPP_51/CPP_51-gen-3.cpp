    string result = "";
    for(int i = 0; i < text.length(); i++){
        if(text[i] != 'a' && text[i] != 'e' && text[i] != 'i' && text[i] != 'o' && text[i] != 'u' && text[i] != 'A' && text[i] != 'E' && text[i] != 'I' && text[i] != 'O' && text[i] != 'U'){
            result += text[i];
        }
    }
    return result;
}

int main(){
    string s = "abcdef\nghijklm";
    cout << remove_vowels(s) << endl;
    return 0;
}

B:
    #include <iostream>
    #include <string>
    #include <cctype>
    using namespace std;

    string remove_vowels(string text) {
        string result;
        for (char c : text) {
            if (isalpha(c) && (tolower(c) != 'a' && tolower(c) != 'e' && tolower(c) != 'i' && tolower(c) != 'o' && tolower(c) != 'u')) {
                result += c;
            }
        }
        return result;
    }

    int main() {
        string s = "abcdef\nghijklm";
        cout << remove_vowels(s) << endl;
        return 0;
    }

C:
    #include <iostream>
    #include <string>
    #include <cctype>
    using namespace std;

    string remove_vowels(string text) {
        string result;
        for (char& c : text) {
            if (!isalpha(c) || (tolower(c) == 'a' || tolower(c) == 'e' || tolower(c) == 'i' || tolower(c) == 'o' || tolower(c) == 'u')) {
                continue;
            }
            result += tolower(c);
        }
        return result;
    }

    int main() {
        string s = "abcdef\nghijklm";
        cout << remove_vowels(s) << endl;
        return 0;
    }

D:
    #include <iostream>
    #include <string>
    #include <cctype>
    using namespace std;

    string remove_vowels(string text) {
        string result;
        for (char& c : text) {
            if (is