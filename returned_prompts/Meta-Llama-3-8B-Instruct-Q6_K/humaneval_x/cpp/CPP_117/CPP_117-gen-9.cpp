    vector<string> result;
    for(string word : split(s," ")){
        int consonants = 0;
        for(char c : word){
            if(c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != ' '){
                consonants++;
            }
        }
        if(consonants == n){
            result.push_back(word);
        }
    }
    return result;
}
vector<string> split(const string& str, const string& delimiter) {
    size_t pos = 0;
    size_t prev = 0;
    vector<string> res;

    while ((pos = str.find(delimiter, prev)) != string::npos) {
        res.push_back(str.substr(prev, pos - prev));
        prev = pos + delimiter.size();
    }
    res.push_back(str.substr(prev));
    return res;
}

int main(){
    string s = "Mary had a little lamb";
    int n = 4;
    vector<string> res = select_words(s,n);
    for(string r : res){
        printf("%s\n",r.c_str());
    }
    return 0;
}

B:
    vector<string> select_words(string s, int n) {
        vector<string> result;
        vector<string> words = split(s, " ");
        for (string word : words) {
            int consonants = 0;
            for (char c : word) {
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != ' ') {
                    consonants++;
                }
            }
            if (consonants == n) {
                result.push_back(word);
            }
        }
        return result;
    }

    vector<string> split(const string& str, const string& delimiter) {
        vector<string> res;
        size_t pos = 0;
        size_t prev = 0;
        while ((pos = str.find(delimiter, prev)) != string::npos) {
            res.push_back(str.substr(prev, pos - prev));
            prev = pos + delimiter.size();
        }
        res.push_back(str.substr(prev));
        return res;
    }

    int main() {
        string s = "Mary had a little lamb";
        int n = 4;
        vector<string> res = select_words(s, n);
        for (string r : res) {
