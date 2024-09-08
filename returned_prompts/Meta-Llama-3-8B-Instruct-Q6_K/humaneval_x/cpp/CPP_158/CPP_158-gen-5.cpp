    string result;
    string max_word;
    int max_count = 0;
    for (int i = 0; i < words.size(); i++) {
        string word = words[i];
        int count = 0;
        set<char> unique_chars(word.begin(), word.end());
        if(unique_chars.size() > max_count){
            max_count = unique_chars.size();
            max_word = word;
            result = word;
        }
    }
    return result;
}

int main() {
    vector<string> words = {"name", "of", "string"};
    printf("%s\n", find_max(words).c_str());
    return 0;
}
