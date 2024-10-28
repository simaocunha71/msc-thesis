    vector<int> music_notes;
    string current_note;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        char chr=music_string[i];
        if (chr=='o')
        {
            current_note+=chr;
            if (i+1<music_string.length())
            {
            char chr1=music_string[i+1];
            if (chr1=='|')
            {
                music_notes.push_back(2);
                i+=1;
            }else
            {
                music_notes.push_back(4);
            }
            }else
            {
                music_notes.push_back(4);
            }
        }
        if (chr=='.')
        {
            current_note+=chr;
            if (i+1<music_string.length())
            {
            char chr1=music_string[i+1];
            if (chr1=='|')
            {
                music_notes.push_back(1);
                i+=1;
            }
            }
        }
    }
    return music_notes;
}

