    int n = txt.size();
    if(n==0) return vector<string>(1, "0");
    int i=0;
    for(;i<n;i++) if(txt[i] == ' ' || txt[i] == ',') break;
    if(i==n) {
        vector<string> v;
        for(int i=0;i<26;i++) if((i+1) % 2 == 1) v.push_back("1");
        return v;
    }
    string word = "";
    word += txt[i];
    for(i++;i<n;i++) if(txt[i] == ' ' || txt[i] == ',') {
        word += txt[i];
        txt[i] = ' ';
    }
    txt[i] = 0;
    vector<string> v;
    v.push_back(word);
    for(i++;i<n;i++) if(txt[i] != ' ') v.push_back(string(1,txt[i]));
    return v;
}


int main() {
    printf("%s\n", split_words("Hello world!").data());
    printf("%s\n", split_words("Hello,world!").data());
    printf("%s\n", split_words("abcdef").data());
    return 0;
}


ANSWER:
vector<string> split_words(string txt) {
    int n = txt.size();
    if (n == 0) return vector<string>(1, "0");
    int i = 0;
    for (; i < n; i++) if (txt[i] == ' ' || txt[i] == ',') break;
    if (i == n) {
        vector<string> v;
        for (int i = 0; i < 26; i++) if ((i + 1) % 2 == 1) v.push_back("1");
        return v;
    }
    string word = "";
    word += txt[i];
    for (i++; i < n; i++) if (txt[i]