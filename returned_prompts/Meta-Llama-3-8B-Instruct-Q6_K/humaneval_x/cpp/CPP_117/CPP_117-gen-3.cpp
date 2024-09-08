    vector<string> result;
    for(int i = 0; i < s.length(); i++){
        string word = "";
        while(i < s.length() && s[i] != ' '){
            word += s[i];
            i++;
        }
        int consonants = 0;
        for(int j = 0; j < word.length(); j++){
            char c = tolower(word[j]);
            if(c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u'){
                consonants++;
            }
        }
        if(consonants == n){
            result.push_back(word);
        }
    }
    return result;
} 

B:
    vector<string> result;
    for(auto word : split(s, ' ')){
        int consonants = 0;
        for(auto c : word){
            char ch = tolower(c);
            if(ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u'){
                consonants++;
            }
        }
        if(consonants == n){
            result.push_back(word);
        }
    }
    return result;
}

int main() {
    // Test the function
    string s1 = "Mary had a little lamb";
    int n1 = 4;
    vector<string> result1 = select_words(s1, n1);
    for(auto word : result1) {
        cout << word << endl;
    }
    cout << endl;

    string s2 = "Mary had a little lamb";
    int n2 = 3;
    vector<string> result2 = select_words(s2, n2);
    for(auto word : result2) {
        cout << word << endl;
    }
    cout << endl;

    string s3 = "simple white space";
    int n3 = 2;
    vector<string> result3 = select_words(s3, n3);
    for(auto word : result3) {
        cout << word << endl;
    }
    cout << endl;

    string s4 = "Hello world";
    int n4 = 4;
    vector<string> result4 = select_words(s4, n4);
    for(auto word : result4) {
        cout << word << endl;
    }
    cout << endl;

    string s5 = "Uncle sam";
    int n5 = 3;
    vector<string> result5