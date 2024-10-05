    vector<int> freq(256, 0);
    int i;
    for  (i=0; i<str.size(); i++)
        freq[tolower(str[i])]++;
    int count = 0;
    for  (i=0; i<256; i++)
        if  (freq[i] != 0)
            count++;
    return count;
}

