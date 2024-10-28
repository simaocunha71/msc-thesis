    vector<int> all_notes;
    string current_note;
    char chr;
    int i;
    int level=0;
    for (i=0;i<music_string.length();i++)
    {
        chr=music_string[i];
        if (chr=='o')
        {
            level+=4;
            current_note+=chr;
        }
        if (chr=='|')
        {
            if (music_string[i-1]=='o')
            {
                level+=2;
                current_note+=chr;
            }
            if (music_string[i-1]=='.')
            {
                level+=1;
                current_note+=chr;
            }
        }
        if (level==4)
        {
            all_notes.push_back(4);
            level=0;
        }
        if (level==2)
        {
            all_notes.push_back(2);
            level=0;
        }
        if (level==1)
        {
            all_notes.push_back(1);
            level=0;
        }
    }
    return all_notes;
}

