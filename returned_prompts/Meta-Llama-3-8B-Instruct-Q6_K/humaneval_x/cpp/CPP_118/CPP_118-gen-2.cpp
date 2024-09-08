    int n = word.size();
    for(int i = n-1; i >= 1; i--){
        if(isvowel(word[i])){
            if(isvowel(word[i-1]) || !isconsonant(word[i-1])){
                return string(1, word[i]);
            }
        }
    }
    return "";
}

bool isvowel(char c){
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

bool isconsonant(char c){
    c = tolower(c);
    return !isvowel(c);
}

int main()
{
    string word;
    printf("Enter the word: ");
    cin >> word;
    cout << get_closest_vowel(word) << endl;
    return 0;
}
