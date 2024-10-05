    if(strings.empty())
        return "";
B:
    string longest = strings[0];
    for(unsigned int i = 1; i < strings.size(); i++){
        if(strings[i].length() > longest.length())
            longest = strings[i];
    }
C:
    return longest;
}
int main() {
    vector<string> v1 = {"a", "b", "c"};
    vector<string> v2 = {"a", "bb", "ccc"};
    vector<string> v3 = {};
    printf("%s\n", longest(v1).c_str());
    printf("%s\n", longest(v2).c_str());
    printf("%s\n", longest(v3).c_str());
    return 0;
}
