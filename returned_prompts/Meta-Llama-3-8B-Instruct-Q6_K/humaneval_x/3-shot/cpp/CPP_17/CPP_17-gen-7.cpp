    vector<int> beats;
    string current_note;
    int beats_per_note;
    for (int i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='.')
        {
            beats.push_back(1);
        }
        else if (music_string[i]=='o')
        {
            beats.push_back(4);
        }
        else if (music_string[i]=='|')
        {
            if (current_note.length()>0)
            beats.push_back(beats_per_note);
            current_note="";
            beats_per_note=0;
        }
        else
        {
            current_note+=music_string[i];
        }
    }
    if (current_note.length()>0)
    beats.push_back(beats_per_note);
    return beats;
}