    vector<string> result;
    for(const auto& str : strings){
        if(str.find(prefix) == 0) {
            result.push_back(str);
        }
    }
    return result;
}

int main() {
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> result = filter_by_prefix(strings, prefix);
    for(const auto& str : result) {
        printf("%s\n", str.c_str());
    }
    return 0;
}
