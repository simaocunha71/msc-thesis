    vector<int> beats;
    string current_beat="";
    int i;
    for (i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='o')
        {
            current_beat=music_string[i];
            if (music_string[i+1]=='|')
            {
                current_beat+="|";
                beats.push_back(2);
                i++;
            }
            else beats.push_back(4);
        }
        if (music_string[i]=='.')
        {
            current_beat=music_string[i];
            if (music_string[i+1]=='|')
            {
                current_beat+="|";
                beats.push_back(1);
                i++;
            }
        }
    }
    return beats;
}

