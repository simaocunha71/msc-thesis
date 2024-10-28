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
        if (chr=='o'&&i+1<music_string.length()&&music_string[i+1]=='|')
        {
            all_notes.push_back(2);
            i+=1;
        }
        if (chr=='.'&&i+1<music_string.length()&&music_string[i+1]=='|')
        {
            all_notes.push_back(1);
            i+=1;
        }
    }
    return all_notes;
}


