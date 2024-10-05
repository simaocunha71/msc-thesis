    vector<string> result;
    for(int i = 0; i < strings.size(); i++){
        if(strings[i].find(substring) != string::npos){
            result.push_back(strings[i]);
        }
    }
    return result;
}
*/

int main() {
    vector<string> strings = {"abc", "bacd", "cde", "vector"};
    string substring = "a";
    vector<string> result = filter_by_substring(strings, substring);
    for(int i = 0; i < result.size(); i++){
        printf("%s\n", result[i].c_str());
    }
    return 0;
}

/*
