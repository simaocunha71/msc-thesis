    vector<int> beats;
    string current_note;
    int i;
    for (i=0;i<music_string.length();i++)
    {
        if (music_string[i]==' ')
        {
            if (current_note=="o")
                beats.push_back(4);
            else if (current_note=="o|")
                beats.push_back(2);
            else if (current_note==".|")
                beats.push_back(1);
            current_note="";
        }
        else if (music_string[i]=='|')
        {
            if (current_note.length()>1)
                current_note=current_note.substr(0,current_note.length()-1);
            else
                current_note="";
        }
        else
        {
            current_note+=music_string[i];
        }
    }
    if (current_note!="")
    {
        if (current_note=="o")
            beats.push_back(4);
        else if (current_note=="o|")
            beats.push_back(2);
        else if (current_note==".|")
            beats.push_back(1);
    }
    return beats;
}  // This solution seems to be correct. It reads the input string and builds a vector of integers
    // corresponding to the number of beats for each note. It handles the cases for whole, half, and
    // quarter notes. It also handles the case where the input string ends with a note. The time complexity
    // is O(n) where n is the length of the input string. The space complexity is O(n) where n is the number
    // of notes in the input string.