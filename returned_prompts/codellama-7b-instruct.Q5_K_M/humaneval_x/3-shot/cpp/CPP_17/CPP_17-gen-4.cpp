    vector<int> beats;
    char chr;
    int i;
    int current_beat;
    for (i=0;i<music_string.length();i++)
    {
        chr=music_string[i];
        if (chr=='o')
        {
        current_beat=4;
        beats.push_back(current_beat);
        }
        if (chr=='|')
        {
            if (music_string[i-1]=='o')
            {
                current_beat=2;
                beats.push_back(current_beat);
            }
            if (music_string[i-1]=='.')
            {
                current_beat=1;
                beats.push_back(current_beat);
            }
        }
    }
    return beats;
}


