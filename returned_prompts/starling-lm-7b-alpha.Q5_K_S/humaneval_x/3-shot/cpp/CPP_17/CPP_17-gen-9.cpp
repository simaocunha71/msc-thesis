    vector<int> all_notes;
    char chr;
    int number=0;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        chr=music_string[i];
        if (chr=='o')
        {
            number=4;
        }
        if (chr=='o|')
        {
            number=2;
        }
        if (chr=='.|')
        {
            number=1;
        }
        all_notes.push_back(number);
    }
    return all_notes;
}



