    vector<string> all_p;
    for(int i = 0; i <= str.length(); i++) {
        all_p.push_back(str.substr(0, i));
    }
    return all_p;
}