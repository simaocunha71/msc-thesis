    vector<string> words;
    vector<string> result;
    string temp = "";

    // Split the string into words
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ' ') {
            words.push_back(temp);
            temp = "";
        } else {
            temp += s[i];
        }
    }
    words.push_back(temp);

    // Check each word if it contains exactly n consonants
    for (string word : words) {
        int count = 0;
        for (char c : word) {
            if (tolower(c) != 'a' && tolower(c) != 'e' && tolower(c) != 'i'
            && tolower(c) != 'o' && tolower(c) != 'u' && isalpha(c)) {
                count++;
            }
        }
        if (count == n) {
            result.push_back(word);
        }
    }
    return result;
}
B:

int main() {
    vector<string> words = select_words("Mary had a little lamb", 4);
    for (string word : words) {
        printf("%s ", word.c_str());
    }
    return 0;
}
C:
// Test the function with different cases
int main() {
    vector<string> words = select_words("Mary had a little lamb", 4);
    for (string word : words) {
        printf("%s ", word.c_str());
    }
    printf("\n");

    words = select_words("Mary had a little lamb", 3);
    for (string word : words) {
        printf("%s ", word.c_str());
    }
    printf("\n");

    words = select_words("simple white space", 2);
    for (string word : words) {
        printf("%s ", word.c_str());
    }
    printf("\n");

    words = select_words("Hello world", 4);
    for (string word : words) {