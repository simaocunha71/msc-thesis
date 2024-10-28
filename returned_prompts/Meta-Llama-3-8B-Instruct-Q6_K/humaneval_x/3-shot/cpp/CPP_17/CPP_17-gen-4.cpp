    vector<int> beats;
    int i=0;
    while (i<music_string.length())
    {
        if (music_string[i]=='o')
        {
            beats.push_back(4);
            i+=1;
        }
        else if (music_string[i]=='o'|')
        {
            beats.push_back(2);
            i+=2;
        }
        else if (music_string[i]=='.')
        {
            beats.push_back(1);
            i+=1;
        }
        else
        {
            printf("Invalid note: %c\n", music_string[i]);
        }
    }
    return beats;
} 





