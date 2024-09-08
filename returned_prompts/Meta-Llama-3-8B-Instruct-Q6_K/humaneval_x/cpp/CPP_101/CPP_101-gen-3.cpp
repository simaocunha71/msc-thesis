    vector<string> result;
    string word = "";
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ',' || s[i] == ' ') {
            if (!word.empty()) {
                result.push_back(word);
                word = "";
            }
        } else {
            word += s[i];
        }
    }
    if (!word.empty()) {
        result.push_back(word);
    }
    return result;
}

B:
    vector<string> words_string(string s){
        vector<string> result;
        string word;
        for (char c : s) {
            if (c == ',' || c == ' ') {
                if (!word.empty()) {
                    result.push_back(word);
                    word = "";
                }
            } else {
                word += c;
            }
        }
        if (!word.empty()) {
            result.push_back(word);
        }
        return result;
    }

C:
    vector<string> words_string(string s){
        vector<string> result;
        stringstream ss(s);
        string word;
        while (ss >> word) {
            result.push_back(word);
        }
        return result;
    }

D:
    vector<string> words_string(string s){
        vector<string> result;
        istringstream iss(s);
        string word;
        while (getline(iss, word, ',')) {
            result.push_back(word);
        }
        return result;
    }

E:
    vector<string> words_string(string s){
        vector<string> result;
        istringstream iss(s);
        string word;
        while (getline(iss, word)) {
            result.push_back(word);
        }
        return result;
    }  
}
}  // namespace std;
int main() {
    // Test your function
    string s1 = "Hi, my name is John";
    string s2 = "One, two, three, four, five, six";
    vector<string> result1 = words_string(s1);
    vector<string> result2 = words_string(s2);
    for (string word : result1) {
        printf("%s\n", word.c_str());
    }
    for (string word : result2) {
        printf("%s\n", word.c_str());
    }
    return 0;
}

The correct answer is C:

The code in option C correctly splits the string into words. It uses the stringstream class to iterate over the words in the string. The stringstream class is a stream class to operate on strings. It