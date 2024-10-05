    sort(words.begin(), words.end(), [](string a, string b) {
        return (int)a.size() > (int)b.size();
    });
    for (string& w : words) {
        int cnt = 0;
        for (char c : w) {
            bool found = false;
            for (char d : w) {
                if (c == d) {
                    found = true;
                    break;
                }
            }
            if (!found) cnt++;
        }
        w = to_string(cnt);
    }
    sort(words.begin(), words.end(), [](string a, string b) {
        if (a == b) return a < b;
        return a.size() > b.size();
    });
    return words[0];
}

int main() {
    vector<string> words = {
        "name", "of", "string",
        "enam", "game",
        "aaaaaaa", "bb", "cc"
    };
    printf("%s\n", find_max(words).c_str());
    return 0;
}





/*

int main() {
    vector<string> words = {
        "name", "of", "string",
        "enam", "game",
        "aaaaaaa", "bb", "cc"
    };
    printf("%s\n", find_max(words).c_str());
    return 0;
}





















































*/

































































































