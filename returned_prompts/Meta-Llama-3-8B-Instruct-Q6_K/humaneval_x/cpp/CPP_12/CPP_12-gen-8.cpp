    if(strings.empty()) {
        return "";
    }
    string longest_str = strings[0];
    for(auto str : strings) {
        if(str.length() > longest_str.length()) {
            longest_str = str;
        }
    }
    return longest_str;
}
int main() {
    vector<string> s = {"a", "bb", "ccc"};
    printf("%s\n", longest(s).c_str());
    return 0;
}

