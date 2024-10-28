    vector<int> beats;
    char chr;
    char note;
    int beats_now=0;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        chr=music_string[i];
        if (chr=='o')
        {
            beats_now=4;
            note='o';
        }
        if (chr=='o|')
        {
            beats_now=2;
            note='o';
        }
        if (chr=='.|')
        {
            beats_now=1;
            note='.';
        }
        if (beats_now>0)
        {
            beats.push_back(beats_now);
            beats_now=0;
        }
    }
    return beats;
}



