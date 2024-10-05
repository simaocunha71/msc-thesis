    vector<string> words;
    vector<string> result;
    string word = "";
    for(char c:s){
        if(c == ' '){
            words.push_back(word);
            word = "";
        }else{
            word += c;
        }
    }
    words.push_back(word);
    for(string w:words){
        int cnt = 0;
        for(char ch:w){
            if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') continue;
            cnt++;
        }
        if(cnt == n) result.push_back(w);
    }
    return result;
}

int main() {
    vector<string> words = select_words("Mary had a little lamb", 4);
    for(string word:words){
        printf("%s ", word.c_str());
    }
    return 0;
}
*/
















































































































































































































































































