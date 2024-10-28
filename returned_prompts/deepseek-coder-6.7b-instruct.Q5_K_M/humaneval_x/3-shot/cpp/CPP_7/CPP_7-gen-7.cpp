    vector<string> filtered_strings;
    int i;
    size_t found;
    for(i=0;i<strings.size();i++){
        found=strings[i].find(substring);
        if(found != string::npos)
            filtered_strings.push_back(strings[i]);
    }
    return filtered_strings;
}


