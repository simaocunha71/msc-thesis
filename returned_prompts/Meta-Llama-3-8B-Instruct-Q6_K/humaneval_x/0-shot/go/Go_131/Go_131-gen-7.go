    int max_count=0;
    string max_word="";
    for(int i=0; i<words.size(); i++){
        int count = 0;
        set<char> s;
        for(int j=0; j<words[i].size(); j++){
            if(s.find(words[i][j]) == s.end()){
                count++;
                s.insert(words[i][j]);
            }
        }
        if(count > max_count){
            max_count = count;
            max_word = words[i];
        }
    }
    return max_word;
}

B:
    vector<string> words = {"name", "of", "string"};
    string result = find_max(words);
    cout << result << endl;

C:
    int main() {
        vector<string> words = {"name", "of", "string"};
        string result = find_max(words);
        cout << result << endl;
        return 0;
    }

D:
    int main() {
        vector<string> words = {"name", "enam", "game"};
        string result = find_max(words);
        cout << result << endl;
        return 0;
    }

E:
    int main() {
        vector<string> words = {"aaaaaaa", "bb", "cc"};
        string result = find_max(words);
        cout << result << endl;
        return 0;
    }F:
    int main() {
        vector<string> words = {"name", "enam", "game"};
        string result = find_max(words);
        cout << result << endl;
        return 0;
    }

F:
    int main() {
        vector<string> words = {"name", "of", "string"};
        string result = find_max(words);
        cout << result << endl;
        return 0;
    }

G:
    int main() {
        vector<string> words = {"aaaaaaa", "bb", "cc"};
        string result = find_max(words);
        cout << result << endl;
        return 0;
    }

H:
    int main() {
        vector<string> words = {"name", "enam", "game"};
        string result = find_max(words);
        cout << result << endl;
        return 0;
    }

I:
    int main() {
        vector<string> words = {"name", "of", "string"};
        string result = find_max(words);
        cout << result << endl;
        return 0;
    }

J:
    int main() {
        vector<string