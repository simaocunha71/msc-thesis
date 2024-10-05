    vector<string> filtered;
    for(int i = 0; i < strings.size(); i++){
        if(strings[i].substr(0, prefix.size()) == prefix){
            filtered.push_back(strings[i]);
        }
    }
    return filtered;
}

int main(){
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    vector<string> filtered = filter_by_prefix(strings, "a");
    for(int i = 0; i < filtered.size(); i++){
        printf("%s\n", filtered[i].c_str());
    }
    return 0;
}
```

