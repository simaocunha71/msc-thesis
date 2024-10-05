    vector<int> beats;
    int length=music_string.length();
    int i;
    for (i=0;i<length;i++)
    {
        if (music_string[i]=='o')
        {
            beats.push_back(4);
            i+=2;
        }
        if (music_string[i]=='|')
        {
            i+=1;
        }
        if (music_string[i]=='.')
        {
            beats.push_back(1);
            i+=2;
        }
    }
    return beats;
}



