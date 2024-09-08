    string result = "";
    string words[sentence.length()];
    int i = 0;
    int j = 0;
    while(i < sentence.length()){
        if(sentence[i] == ' '){
            i++;
            continue;
        }
        words[j] = "";
        while(i < sentence.length() && sentence[i] != ' '){
            words[j] += sentence[i];
            i++;
        }
        j++;
    }
    for(int i = 0; i < j; i++){
        int len = words[i].length();
        bool is_prime = true;
        for(int j = 2; j*j <= len; j++){
            if(len % j == 0){
                is_prime = false;
                break;
            }
        }
        if(is_prime){
            result += words[i] + " ";
        }
    }
    return result.substr(0, result.length() - 1);
}
int main() {
    string sentence = "This is a test";
    printf("%s\n", words_in_sentence(sentence).c_str());
    return 0;
}

B:
    #include <iostream>
    #include <vector>
    #include <string>
    #include <algorithm>
    using namespace std;
    string words_in_sentence(string sentence) {
        vector<string> words;
        string word = "";
        for (char c : sentence) {
            if (c == ' ') {
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
        string result = "";
        for (string w : words) {
            int len = w.length();
            bool is_prime = true;
            for (int i = 2; i * i <= len; i++) {
                if (len % i == 0) {
                    is_prime = false;
                    break;
                }
            }
            if (is_prime) {
                result += w + " ";
            }
        }
        return result.substr(0, result.length() - 1);
    }
    int main() {
        string sentence = "This is a test";
        cout << words_in_sentence(sentence) << endl;
        return 0;
    }
C:
    #include <iostream>
    #include <string>
    #include <vector>
    using namespace std;
    string words_in_sentence(string sentence) {
        vector<string