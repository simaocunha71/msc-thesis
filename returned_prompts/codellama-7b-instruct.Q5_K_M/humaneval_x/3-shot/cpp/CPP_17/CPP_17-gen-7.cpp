    vector<int> beats;
    int level=0;
    int current_beat=0;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='o')
        current_beat=4;
        if (music_string[i]=='|')
        current_beat=2;
        if (music_string[i]=='.')
        current_beat=1;
        if (music_string[i]==' ')
        {
            level+=1;
            if (level==1)
            beats.push_back(current_beat);
        }
        if (music_string[i]=='\n')
        {
            level-=1;
            if (level==0)
            beats.push_back(current_beat);
        }
    }
    return beats;
}



