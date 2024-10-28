    vector<int> note_lengths;
    string current_note;
    int length;
    char chr;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        chr=music_string[i];
        if (chr=='o')
        {
            length=4;
        }
        if (chr=='o'||chr=='|')
        {
            current_note+=chr;
        }
        if (current_note.length()>0&&(chr=='.'||chr=='|'))
        {
            note_lengths.push_back(length);
            length=0;
            current_note="";
        }
    }
    if (length>0)
    {
        note_lengths.push_back(length);
    }
    return note_lengths;
}


