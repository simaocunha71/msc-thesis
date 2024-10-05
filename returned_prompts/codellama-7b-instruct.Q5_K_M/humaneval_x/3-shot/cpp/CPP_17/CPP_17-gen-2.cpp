    vector<int> beats;
    int length=music_string.length();
    int i;
    for (i=0;i<length;i++)
    {
        if (music_string[i]=='o')
        beats.push_back(4);
        if (music_string[i]=='|')
        {
            if (music_string[i+1]=='o')
            beats.push_back(2);
            if (music_string[i+1]=='.')
            beats.push_back(1);
        }
    }
    return beats;
}


