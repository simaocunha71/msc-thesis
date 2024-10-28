    vector<int> beats;
    char chr;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        chr=music_string[i];
        if (chr=='o')
        beats.push_back(4);
        if (chr=='o' && music_string[i+1]=='|')
        beats.push_back(2);
        if (chr=='.' && music_string[i+1]=='|')
        beats.push_back(1);
    }
    return beats;
}


