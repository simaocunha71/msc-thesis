    vector<string> words, ans;
    string word = "";
    for (char c: s)
        if (c == ' '){
            words.push_back(word);
            word = "";
        } else word += c;
    if(word.size() > 0) words.push_back(word);
    for (string w: words) {
        int c = 0;
        for (char l: w)
            if (tolower(l) != 'a' && tolower(l) != 'e' && tolower(l) != 'i' && tolower(l) != 'o' && tolower(l) != 'u' && isalpha(l)) c++;
        if (c == n) ans.push_back(w);
    }
    return ans;
}
int main() {
    vector<string> words = select_words("Mary had a little lamb", 4);
    for(string word : words)
        printf("%s ", word.c_str());
    return 0;
}

This program uses C++ to solve the problem. The program begins by splitting the input string into words and storing them in a vector. It then iterates over each word, counting the number of consonants in it. If the count matches the required number, the word is added to the answer vector. Finally, the answer vector is returned.
The C++ function tolower is used to convert letters to lowercase to handle case sensitivity.
The C++ function isalpha is used to check if a character is a letter.
*/

















































































































































