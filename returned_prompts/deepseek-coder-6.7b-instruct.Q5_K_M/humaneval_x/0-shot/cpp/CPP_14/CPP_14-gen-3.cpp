    vector<string> result;
    string prefix;
    for(int i = 0; i < str.size(); i++){
        prefix += str[i];
        result.push_back(prefix);
    }
    return result;
}

int main() {
    string str = "abc";
    vector<string> prefixes = all_prefixes(str);
    for(int i = 0; i < prefixes.size(); i++){
        printf("%s ", prefixes[i].c_str());
    }
    return 0;
}

*/

