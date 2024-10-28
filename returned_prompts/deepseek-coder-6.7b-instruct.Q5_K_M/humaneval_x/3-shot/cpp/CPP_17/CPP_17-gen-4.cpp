    vector<int> beats;
    for (int i=0; i<music_string.length(); i++)
    {
        switch(music_string[i])
        {
            case 'o': beats.push_back(4); break;
            case '|': beats.push_back(2); break;
            case '.': beats.push_back(1); break;
            default : break;
        }
    }
    return beats;
}

