    vector<int> beats;
    int i=0;
    while (i<music_string.length())
    {
    if (music_string[i]=='o')
    {
        beats.push_back(4);
        i+=2;
    }
    if (music_string[i]=='.')
    {
        beats.push_back(1);
        i+=2;
    }
    }
    return beats;
}


