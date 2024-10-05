    vector<string> res;
    int n = s.length();
    for(int i = 0; i < n; i++) {
        if(s[i] == ' ' || s[i] == ',') {
            res.push_back(s.substr(i - 1, 2));
            i++;
            continue A;
        }
        res.push_back(s.substr(i, 1));
    }
    return res;
}
int main() {
    string s = "Hi, my name is John";
    for(string w : words_string(s)) {
        printf("%s ", w.c_str());
    }
    printf("\n");
    s = "One, two, three, four, five, six";
    for(string w : words_string(s)) {
        printf("%s ", w.c_str());
    }
    printf("\n");
}








ANSWER:
vector<string> words_string(string s) {
    vector<string> res;
    int n = s.length();
    for (int i = 0; i < n; i++) {
        if (s[i] == ' ' || s[i] == ',') {
            res.push_back(s.substr(i - 1, 2));
            i++;
            continue;
        }
        res.push_back(s.substr(i, 1));
    }
    return res;
}


























































































































































