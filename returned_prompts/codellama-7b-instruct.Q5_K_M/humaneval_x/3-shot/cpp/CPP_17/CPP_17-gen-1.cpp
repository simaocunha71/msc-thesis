    vector<int> beats;
    int i;
    int beats_count=0;
    int beats_counter=0;
    for (i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='o')
            beats_count=4;
        if (music_string[i]=='|')
            beats_count=2;
        if (music_string[i]=='.')
            beats_count=1;
        beats_counter+=beats_count;
        beats.push_back(beats_counter);
    }
    return beats;
}



