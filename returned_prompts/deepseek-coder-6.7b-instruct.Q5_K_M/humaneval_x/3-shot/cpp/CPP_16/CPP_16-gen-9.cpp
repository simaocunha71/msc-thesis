    vector<int> char_map(256, 0);
    int i;
    for (i=0; i<str.length(); i++)
        char_map[tolower(str[i])] = 1;

    return count(char_map.begin(), char_map.end(), 1);
}

