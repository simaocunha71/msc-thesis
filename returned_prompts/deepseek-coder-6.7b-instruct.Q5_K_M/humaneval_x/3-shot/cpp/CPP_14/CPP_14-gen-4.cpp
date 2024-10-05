    vector<string> prefixes;
    string temp = "";
    for (int i = 0; i < str.size(); i++){
        temp += str[i];
        prefixes.push_back(temp);
    }
    return prefixes;
}


