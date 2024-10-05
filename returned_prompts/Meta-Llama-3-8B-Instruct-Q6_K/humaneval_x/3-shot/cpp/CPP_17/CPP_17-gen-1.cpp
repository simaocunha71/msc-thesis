    vector<int> beat_lengths;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='o')
            beat_lengths.push_back(4);
        else if (music_string[i]=='o'|)
            beat_lengths.push_back(2);
        else if (music_string[i]=='.')
            beat_lengths.push_back(1);
    }
    return beat_lengths;
} 





