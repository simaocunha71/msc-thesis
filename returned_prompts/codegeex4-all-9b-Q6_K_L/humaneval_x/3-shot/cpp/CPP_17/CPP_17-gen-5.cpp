    vector<int> music_vector;
    int beat;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='o')
        {
            beat=4;
        }
        if (music_string[i]=='|')
        {
            if (music_string[i-1]=='o')
            {
                beat=2;
            }
            if (music_string[i-1]=='.')
            {
                beat=1;
            }
        }
        music_vector.push_back(beat);
    }
    return music_vector;
}

