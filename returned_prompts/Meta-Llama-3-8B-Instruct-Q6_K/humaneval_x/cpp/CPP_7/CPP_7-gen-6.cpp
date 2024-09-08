vector<string> result;
for(const string& str : strings){
    if(str.find(substring) != string::npos){
        result.push_back(str);
    }
}
return result;
}
int main() {
    vector<string> strings = {"abc", "bacd", "cde", "vector"};
    string substring = "a";
    vector<string> filtered_strings = filter_by_substring(strings, substring);
    for(const string& str : filtered_strings){
        printf("%s\n", str.c_str());
    }
    return 0;
} 
