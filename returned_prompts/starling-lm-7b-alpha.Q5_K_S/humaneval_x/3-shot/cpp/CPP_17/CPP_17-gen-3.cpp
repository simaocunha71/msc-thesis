    vector<int> all_notes;
    char chr;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        chr=music_string[i];
        if (chr=='o')
        {
        all_notes.push_back(4);
        }
        if (chr=='o|')
        {
        all_notes.push_back(2);
        }
        if (chr=='.|')
        {
        all_notes.push_back(1);
        }
    }
    return all_notes;
}


