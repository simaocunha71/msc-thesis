    vector<int> beats;
    int current_beat;
    string current_note;
    for (int i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='.')
        {
            current_note+=".";
        }
        if (music_string[i]=='o')
        {
            current_note+="o";
        }
        if (music_string[i]=='|')
        {
            if (current_note.length()==1)
            {
                beats.push_back(1);
                current_beat=1;
                current_note="";
            }
            else if (current_note.length()==2)
            {
                beats.push_back(2);
                current_beat=2;
                current_note="";
            }
            else
            {
                beats.push_back(4);
                current_beat=4;
                current_note="";
            }
        }
    }
    return beats;
}
