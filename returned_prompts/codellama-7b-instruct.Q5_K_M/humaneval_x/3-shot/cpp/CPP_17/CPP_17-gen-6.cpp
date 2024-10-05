    vector<int> music;
    int level=0;
    int i;
    int beats=0;
    for (i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='o')
        {
            beats=4;
        }
        if (music_string[i]=='|')
        {
            level-=1;
            if (level==0)
            {
                music.push_back(beats);
                beats=0;
            }
        }
        if (music_string[i]==' ')
        {
            level+=1;
        }
    }
    music.push_back(beats);
    return music;
}



