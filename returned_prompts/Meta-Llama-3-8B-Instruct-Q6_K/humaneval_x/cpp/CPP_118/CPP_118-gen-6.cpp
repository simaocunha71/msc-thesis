    // sort the string by reverse order
    sort(word.begin(), word.end(), greater<char>());

    // initialize the index of the word
    int i = 0;
    while(i < word.length()) {
        // check if the current character is vowel
        if(word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u' || word[i] == 'A' || word[i] == 'E' || word[i] == 'I' || word[i] == 'O' || word[i] == 'U') {
            // check if the previous and the next character are consonant
            if(i > 0 && !((word[i-1] >= 'a' && word[i-1] <= 'z') || (word[i-1] >= 'A' && word[i-1] <= 'Z'))) {
                if(i+1 < word.length() && !((word[i+1] >= 'a' && word[i+1] <= 'z') || (word[i+1] >= 'A' && word[i+1] <= 'Z'))) {
                    // return the vowel
                    return word.substr(i);
                }
            }
        }
        i++;
    }
    return "";
}
int main() {
    printf("%s\n", get_closest_vowel("yogurt").c_str());
    printf("%s\n", get_closest_vowel("FULL").c_str());
    printf("%s\n", get_closest_vowel("quick").c_str());
    printf("%s\n", get_closest_vowel("ab").c_str());
    return 0;
}
