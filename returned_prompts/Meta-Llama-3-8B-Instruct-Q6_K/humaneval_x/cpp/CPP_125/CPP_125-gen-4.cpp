    // Split string into words using whitespace
    vector<string> words;
    string word;
    for (char c : txt) {
        if (c == ' ') {
            if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        } else if (c == ',') {
            if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        } else {
            word += c;
        }
    }
    if (!word.empty()) {
        words.push_back(word);
    }
    
    // If no words found, count the number of lower-case letters with odd order in the alphabet
    if(words.empty()){
        int count = 0;
        for(int i = 0; i < 26; i++){
            if('a' + i <= txt[0] && txt[0] <= 'z' + i){
                count++;
            }
        }
        words.push_back(to_string(count));
    }
    return words;
}

int main(){
    string s1 = "Hello world!";
    string s2 = "Hello,world!";
    string s3 = "abcdef";
    vector<string> res1 = split_words(s1);
    vector<string> res2 = split_words(s2);
    vector<string> res3 = split_words(s3);
    printf("res1: %s\n", res1[0].c_str());
    printf("res1: %s\n", res1[1].c_str());
    printf("res2: %s\n", res2[0].c_str());
    printf("res2: %s\n", res2[1].c_str());
    printf("res3: %s\n", res3[0].c_str());
    return 0;
}

B:
    #include <iostream>
    #include <vector>
    #include <string>
    #include <algorithm>
    #include <cctype>

    using namespace std;

    vector<string> split_words(string txt) {
        vector<string> words;

        // Split string into words using whitespace
        string word;
        for (char c : txt) {
            if (isspace(c) || c == ',') {
                if (!word.empty()) {
                    words.push_back(word);
                    word.clear();
                }
                if (c == ',') break;
            } else {
                word += c;
            }
        }
        if (!word.empty()) {
            words.push_back(word);
       