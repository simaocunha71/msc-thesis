    vector<string> result;
    for(const auto &str: strings){
        if(str.find(substring) != string::npos){
            result.push_back(str);
        }
    }
    return result;
}

int main(){
    vector<string> strings = {"abc", "bacd", "cde", "vector"};
    string substring = "a";
    vector<string> result = filter_by_substring(strings, substring);
    for(const auto &str: result){
        printf("%s\n", str.c_str());
    }
    return 0;
}
*/

