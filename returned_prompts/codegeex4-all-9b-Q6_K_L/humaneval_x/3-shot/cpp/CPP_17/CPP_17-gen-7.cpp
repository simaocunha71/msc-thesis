    vector<int> all_notes;
    string note;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='o')
        {
            note="o";
            if (i+1<music_string.length()&&music_string[i+1]=='|')
            {
                note+="|";
                all_notes.push_back(2);
            }
            else
                all_notes.push_back(4);
        }
        else if (music_string[i]=='.')
        {
            note=".";
            if (i+1<music_string.length()&&music_string[i+1]=='|')
            {
                note+="|";
                all_notes.push_back(1);
            }
        }
    }
    return all_notes;
}

