    vector<int> beats;
    int level=0;
    char chr;
    int i;
    int current_beat=0;
    for (i=0;i<music_string.length();i++)
    {
        chr=music_string[i];
        if (chr=='o')
        {
            if (level==0)
            beats.push_back(4);
            if (level==1)
            beats[beats.size()-1]=beats[beats.size()-1]*2;
            if (level==2)
            beats[beats.size()-1]=beats[beats.size()-1]*4;
        }
        if (chr=='|')
        level+=1;
        else
        level-=1;
    }
    return beats;
}


