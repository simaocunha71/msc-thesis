    vector<int> char_map(128,0);
    transform(str.begin(), str.end(), str.begin(), ::toupper);
    for(char& c : str)
    {
        char_map[int(c)]=1;
    }
    return accumulate(char_map.begin(), char_map.end(), 0);
}


