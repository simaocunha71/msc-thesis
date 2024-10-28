    vector<int> beats;
    string note;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        note="";
        while (i<music_string.length() && music_string[i]!='|')
        {
            note+=music_string[i];
            i++;
        }
        i++;
        if (note=="o")
            beats.push_back(4);
        else if (note=="o|")
            beats.push_back(2);
        else if (note==".|")
            beats.push_back(1);
    }
    return beats;
}  