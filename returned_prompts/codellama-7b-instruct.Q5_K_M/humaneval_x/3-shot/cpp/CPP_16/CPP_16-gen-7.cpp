    transform(str.begin(), str.end(), str.begin(), ::tolower);
    vector<int> char_count(256, 0);
    for (char c : str)
    char_count[c]++;
    int distinct_count = 0;
    for (int i = 0; i < char_count.size(); i++)
    if (char_count[i])
    distinct_count++;
    return distinct_count;
}


