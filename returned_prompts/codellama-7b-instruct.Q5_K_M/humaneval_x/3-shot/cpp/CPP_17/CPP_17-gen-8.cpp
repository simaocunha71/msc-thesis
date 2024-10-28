    vector<int> beats;
    string current_beat;
    int level=0;
    char chr;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        chr=music_string[i];
        if (chr=='o')
        {
            current_beat="4";
        }
        if (chr=='|')
        {
            current_beat="2";
        }
        if (chr=='.')
        {
            current_beat="1";
        }
        if (chr=='o' || chr=='|' || chr=='.')
        {
            beats.push_back(stoi(current_beat));
            current_beat="";
        }
    }
    return beats;
}








