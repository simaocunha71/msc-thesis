    vector<int> beats;
    string current_note;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        if (music_string[i]=='|')
        {
            if (current_note=="o")
                beats.push_back(4);
            else if (current_note=="o|")
                beats.push_back(2);
            else if (current_note==".|")
                beats.push_back(1);
            current_note="";
        }
        else
        {
            current_note+=music_string[i];
        }
    }
    if (current_note=="o")
        beats.push_back(4);
    else if (current_note=="o|")
        beats.push_back(2);
    else if (current_note==".|")
        beats.push_back(1);
    return beats;
} 
*/



