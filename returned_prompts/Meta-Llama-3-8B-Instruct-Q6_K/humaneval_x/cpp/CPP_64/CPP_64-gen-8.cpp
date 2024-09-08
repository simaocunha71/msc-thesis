    int count = 0;
    for(int i = 0; i < s.length(); i++) {
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || (s[i] == 'y' && i == s.length() - 1)) {
            count++;
        }
    }
    return count;
}
int main() {
    string str;
    cout << "Enter a word: ";
    getline(cin, str);
    cout << "The number of vowels in the word is: " << vowels_count(str);
    return 0;
}
