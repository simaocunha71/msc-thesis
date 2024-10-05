    vector<int> beats;
    string beat_str;
    int beat_length;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='o' || music_string[i]=='o|' || music_string[i]=='.|')
        {
        if (music_string[i]=='o')
        beat_length=4;
        if (music_string[i]=='o|')
        beat_length=2;
        if (music_string[i]=='.|')
        beat_length=1;
        beats.push_back(beat_length);
        }
        else
        {
        beat_str+=music_string[i];
        }
    }
    return beats;
}




