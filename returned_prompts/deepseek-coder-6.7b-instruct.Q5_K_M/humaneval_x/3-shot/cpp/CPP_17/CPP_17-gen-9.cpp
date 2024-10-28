    vector<int> beats;
    string note;
    int i;
    for  (i=0;i<music_string.length();i++)
    {
        if  (music_string[i]==' ')
        {
            if  (note=="o")
                beats.push_back(4);
            if  (note=="o|")
                beats.push_back(2);
            if  (note==".|")
                beats.push_back(1);
            note="";
        }
        else
            note+=music_string[i];
    }
    if  (note=="o")
        beats.push_back(4);
    if  (note=="o|")
        beats.push_back(2);
    if  (note==".|")
        beats.push_back(1);
    return beats;
}


