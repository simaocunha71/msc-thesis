    vector<string> prefixes;
    string prefix = "";
    for(char c : str){
        prefix += c;
        prefixes.push_back(prefix);
    }
    return prefixes;
}


