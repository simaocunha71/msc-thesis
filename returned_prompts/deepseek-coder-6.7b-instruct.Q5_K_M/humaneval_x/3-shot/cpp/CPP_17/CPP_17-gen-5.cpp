    vector<int> beats;
    string beat_string;
    int i;
    for  (i=0;i<music_string.length();i++)
    {
        if  (music_string[i]==' ')
        {
            if  (beat_string=="o")
            beats.push_back(4);
            else if  (beat_string=="o|")
            beats.push_back(2);
            else if  (beat_string==".|")
            beats.push_back(1);
            beat_string="";
        }
        else
        {
            beat_string+=music_string[i];
        }
    }
    if  (beat_string=="o")
    beats.push_back(4);
    else if  (beat_string=="o|")
    beats.push_back(2);
    else if  (beat_string==".|")
    beats.push_back(1);
    return beats;
}

