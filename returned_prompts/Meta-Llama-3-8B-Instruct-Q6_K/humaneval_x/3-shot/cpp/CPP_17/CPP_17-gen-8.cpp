    vector<int> beats;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='o')
            beats.push_back(4);
        if (music_string[i]=='|')
            beats.push_back(beats.back()/2);
    }
    return beats;
} 
